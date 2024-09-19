# created based on speech_xvector_dbs-EER
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve

from sklearn.base import BaseEstimator, ClassifierMixin
from speechbrain.processing.PLDA_LDA import *


class PCA_PLDA_EER_Classifier(BaseEstimator, ClassifierMixin):
    def __init__(self, PCA_n=5, eer_threshold=0.5, scaler=None, pca=None, plda=None, en_stat=None, en_sets=None,
                 normalize=1):
        self.scaler = scaler  # for normalization
        self.PCA_n = PCA_n  # for PCA
        self.pca = pca  # for PCA
        self.plda = plda  # for plda
        self.en_stat = en_stat  # for plda
        self.en_sets = en_sets  # for plda
        self.eer_threshold = eer_threshold  # for final classification
        self.normalize = normalize  # 1 or 0, don't normalize if input feats are pre-normalized

    def fit(self, features_train, train_lbs):
        """
        features_train: np array [N x feature dim]
        train_lbs: a list of labels, 0 or 1
        """
        # PCA------------------------------------------------------------------------
        # Standardize features by removing the mean and scaling to unit variance
        if self.normalize == 1:
            self.scaler = StandardScaler()
            features_train = self.scaler.fit_transform(features_train)  # Nx512

        self.pca = PCA(n_components=self.PCA_n)
       # print("pca applied")
        features_train = self.pca.fit_transform(features_train)  # NxPCA_n

        # speechbrain PLDA--------------------------------------------------------------
        train_lbs_tmp = np.array(train_lbs)
        features_PD = features_train[np.where(train_lbs_tmp == 0)[0]]  # NxPCA_n
        features_HC = features_train[np.where(train_lbs_tmp == 1)[0]]  # NxPCA_n

        # PLDA
        dim, N = self.PCA_n, features_train.shape[0]
        train_xv = features_train
        md = ['md' + str(train_lbs[i]) for i in range(N)]
        modelset = numpy.array(md, dtype="|O")
        sg = ['sg' + str(i) for i in range(N)]
        segset = numpy.array(sg, dtype="|O")
        s = numpy.array([None] * N)
        stat0 = numpy.array([[1.0]] * N)
        xvectors_stat = StatObject_SB(modelset=modelset, segset=segset, start=s, stop=s, stat0=stat0, stat1=train_xv)
        # Training PLDA model: M ~ (mean, F, Sigma)
        self.plda = PLDA(rank_f=dim)
        self.plda.plda(xvectors_stat)

        # PLDA Enrollment (2 classes)
        en_N = 2
        en_pd = np.mean(features_PD, axis=0)
        en_hc = np.mean(features_HC, axis=0)
        en_xv = np.vstack((en_pd, en_hc))
        en_sgs = ['en' + str(i) for i in range(en_N)]
        self.en_sets = numpy.array(en_sgs, dtype="|O")
        en_s = numpy.array([None] * en_N)
        en_stat0 = numpy.array([[1.0]] * en_N)
        self.en_stat = StatObject_SB(modelset=self.en_sets, segset=self.en_sets, start=en_s, stop=en_s, stat0=en_stat0,
                                     stat1=en_xv)

        # get PLDA scores of train data for EER threshold
        va_N = features_train.shape[0]
        va_xv = features_train
        va_sgs = ['va' + str(i) for i in range(va_N)]
        va_sets = numpy.array(va_sgs, dtype="|O")
        va_s = numpy.array([None] * va_N)
        va_stat0 = numpy.array([[1.0]] * va_N)
        va_stat = StatObject_SB(modelset=va_sets, segset=va_sets, start=va_s, stop=va_s, stat0=va_stat0, stat1=va_xv)
        ndx = Ndx(models=self.en_sets, testsegs=va_sets)
        # PLDA Scoring
        scores_plda = fast_PLDA_scoring(self.en_stat, va_stat, ndx, self.plda.mean, self.plda.F, self.plda.Sigma)
        train_X = np.transpose(scores_plda.scoremat)  # [#samples, 2]

        # get equal error rate threshold---------------------------------------------------
        train_pt = np.array([train_X[:, 1] - train_X[:, 0]])  # np.array([train_X[:,0]-train_X[:,1]])
        train_X = np.transpose(train_pt)  # for eer

        fpr, tpr, threshold = roc_curve(train_lbs, train_X, pos_label=1, drop_intermediate=False)
        fnr = 1 - tpr
        self.eer_threshold = threshold[np.nanargmin(np.absolute((fnr - fpr)))]

    def predict_scores(self, features_test):
        """
        (for now apply only when N = 1 to make sure calling of fast_PLDA_scoring is on each test sample individually)

        features_test: np array [N x feature dim]

        return an array of predicted scores, np[1, N]
        """
        # PCA
        # Standardize features by removing the mean and scaling to unit variance
        if self.normalize == 1:
            features_test = self.scaler.transform(features_test)  # Nx512
        # transform
        features_test = self.pca.transform(features_test)  # NxPCA_n
        #print("pca applied")

        # PLDA Test -------------------------------------------------------------------------------------------
        te_N = features_test.shape[0]
        te_xv = features_test
        te_sgs = ['te' + str(i) for i in range(te_N)]
        te_sets = numpy.array(te_sgs, dtype="|O")
        te_s = numpy.array([None] * te_N)
        te_stat0 = numpy.array([[1.0]] * te_N)
        te_stat = StatObject_SB(modelset=te_sets, segset=te_sets, start=te_s, stop=te_s, stat0=te_stat0, stat1=te_xv)
        ndx = Ndx(models=self.en_sets, testsegs=te_sets)
        # PLDA Scoring
        scores_plda = fast_PLDA_scoring(self.en_stat, te_stat, ndx, self.plda.mean, self.plda.F, self.plda.Sigma)
        scores_y = np.transpose(scores_plda.scoremat)  # [#samples, 2]

        # Classification by plda scores with eer threshold ----------------------------------
        test_pt = np.array(scores_y[:, 1] - scores_y[:, 0])  # [N,]
        return test_pt

    def predict_scores_list(self, features_test):
        """
        features_test: np array [N x feature dim]

        return an array of predicted scores [N,1]
        """
        N = features_test.shape[0]
        scores = []
        for i in range(N):
            # check if feat vect contains nan vals,
            # set score as nan if yes
            if np.isnan(features_test[i, 0]):
                scores.append(np.nan)
            else:
                scores.append(self.predict_scores(features_test[[i], :])[0])
        scores = np.array(scores)
        scores = scores[:, np.newaxis]  # [N,] to [N,1]
        return scores

    def predict(self, features_test):
        """
        features_test: np array [N x feature dim]

        return a list of predicted labels, 0 or 1
        """
        predictions = []
        for i in range(features_test.shape[0]):
            test_pt = self.predict_scores(features_test[[i], :])
            if test_pt[0] > self.eer_threshold:
                predictions.append(1)
            else:
                predictions.append(0)

        # test_pt = self.predict_scores(features_test)
        # predictions = list(test_pt[0]<self.eer_threshold) # > threshold pred 0, < threshold then 1
        # predictions = [int(x) for x in predictions]

        return predictions