# PARKCELEB

Great, based on the abstract you provided, here’s a refined GitHub README for the project:

---

# Unveiling Early Signs of Parkinson’s Disease via A Longitudinal Analysis of Celebrity Speech Recordings

## Project Overview

This project investigates the potential for early detection of Parkinson’s Disease (PD) through a longitudinal analysis of speech recordings from celebrities who publicly disclosed their diagnosis. The focus is on creating and utilizing a new corpus, ParkCeleb, which includes longitudinal speech data collected from 40 subjects with PD and 40 controls. By analyzing speech features over a period from 10 years before to 20 years after diagnosis, the project aims to uncover patterns indicative of early PD progression.

## Abstract

Numerous studies proposed methods to detect Parkinson’s Disease (PD) via speech analysis. However, existing corpora often lack prodromal recordings, have small sample sizes, and lack longitudinal data. Speech samples from celebrities who publicly disclosed their PD diagnosis provide longitudinal data, allowing the creation of a new corpus, ParkCeleb. We collected videos from 40 subjects with PD and 40 controls and analyzed evolving speech features from 10 years before to 20 years after diagnosis. Our longitudinal analysis, focused on 15 subjects with PD and 15 controls, revealed features like pitch variability, pause duration, speech rate, and syllable duration, indicating PD progression. Early dysarthria patterns were detectable in the prodromal phase, with the best classifiers achieving AUCs of 0.72 and 0.75 for data collected ten and five years before diagnosis, respectively, and 0.93 post-diagnosis. This study highlights the potential for early detection methods, aiding treatment response identification and screening in clinical trials.

## Objectives

- **Create ParkCeleb Corpus:** Develop a comprehensive corpus of longitudinal speech recordings from PD subjects and controls.
- **Feature Extraction:** Analyze evolving speech features such as pitch variability, pause duration, speech rate, and syllable duration.
- **Early Detection:** Identify early dysarthria patterns and evaluate their effectiveness in predicting PD.
- **Model Evaluation:** Assess machine learning models for classification performance with AUC metrics.

## Dataset

The dataset used in this project consists of:

- **Speech Recordings:** Videos from 40 subjects with Parkinson’s Disease and 40 controls, spanning 10 years before and 20 years after diagnosis.
- **Metadata:** Detailed information about each recording session, including speaker identity and diagnosis timeline.

## Methodology

1. **Data Collection:** Accumulate longitudinal speech recordings from celebrities with diagnosed Parkinson’s Disease and matched controls.
2. **Feature Extraction:** Extract and analyze key speech features indicative of PD progression.
3. **Data Preprocessing:** Clean and organize data for analysis, handling missing values and ensuring consistency.
4. **Analysis:** Perform longitudinal analysis to identify significant changes in speech features related to Parkinson’s Disease.
5. **Model Development:** Train and evaluate machine learning classifiers to detect early signs of PD using extracted speech features.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/early-signs-parkinsons-disease.git](https://github.com/Annafavaro/PARKCELEB.git
   cd PARKCELEB
   ```

2. **Install Dependencies:**

   Create a virtual environment and install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Data:**

   Place speech recordings and metadata files in the specified directories.

2. **Extract Features:**

   Run the feature extraction script:

   ```bash
   python extract_features.py
   ```

3. **Train and Evaluate Models:**

   Execute the model training and evaluation:

   ```bash
   python train_model.py
   ```

4. **Analyze Results:**

   Perform longitudinal analysis and view results:

   ```bash
   python analyze_results.py
   ```

## Results

- **Feature Analysis:** Insights into key speech features associated with Parkinson’s Disease progression.
- **Model Performance:** Evaluation of classifiers with AUC scores ranging from 0.72 to 0.93 depending on the time relative to diagnosis.
- **Early Detection:** Identification of dysarthria patterns detectable in the prodromal phase.

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter issues, please open an issue or submit a pull request. Refer to the `CONTRIBUTING.md` file for detailed guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Data Sources:** Acknowledge sources of data and contributions.
- **Funding:** Mention any grants or funding sources if applicable.

## Contact

For questions or further information, please contact [Anna Favaro](mailto:afavaro1@jhu.edu).
