# Unveiling Early Signs of Parkinson’s Disease via A Longitudinal Analysis of Celebrity Speech Recordings 

## Overview

This project investigates the potential for early detection of Parkinson’s Disease (PD) through a longitudinal analysis of speech recordings from celebrities who publicly disclosed their diagnosis. The focus is on creating and utilizing a new corpus, ParkCeleb, which includes longitudinal speech data collected from 40 subjects with PD and 40 controls. By analyzing speech features over a period from 10 years before to 20 years after diagnosis, the project aims to uncover patterns indicative of early PD progression.

## Abstract

Numerous studies proposed methods to detect Parkinson’s Disease (PD) via speech analysis. However, existing corpora often lack prodromal recordings, have small sample sizes, and lack longitudinal data. Speech samples from celebrities who publicly disclosed their PD diagnosis provide longitudinal data, allowing the creation of a new corpus, ParkCeleb. We collected videos from 40 subjects with PD and 40 controls and analyzed evolving speech features from 10 years before to 20 years after diagnosis. Our longitudinal analysis, focused on 15 subjects with PD and 15 controls, revealed features like pitch variability, pause duration, speech rate, and syllable duration, indicating PD progression. Early dysarthria patterns were detectable in the prodromal phase, with the best classifiers achieving AUCs of 0.72 and 0.75 for data collected ten and five years before diagnosis, respectively, and 0.93 post-diagnosis. This study highlights the potential for early detection methods, aiding treatment response identification and screening in clinical trials.

## Objectives

- **Create ParkCeleb Corpus:** Develop a comprehensive corpus of longitudinal speech recordings from PD subjects and controls.
- **Feature Extraction:** Analyze evolving speech features such as pitch variability, pause duration, speech rate, and syllable duration.
- **Early Detection:** Identify early dysarthria patterns and evaluate their effectiveness in predicting PD.
- **Model Evaluation:** Assess machine learning models for classification performance with AUC metrics.

## ParkCeleb :dizzy:

The **ParkCeleb** data set is stored in the following [Zenodo repository](link). This repo does not contain the actual audio recordings but provides metadata files with links to YouTube videos, speaker information, and transcriptions. Below is an explanation of the folder structure and how to work with the provided files to download and process the data.

### Folder Structure

Each speaker has an anonymized folder named after their ID (e.g., `cn_01` for controls or `pd_01` for Parkinson’s Disease subjects). Inside each speaker's folder, you will find:

- **`metadata.csv`**: A file containing YouTube video links for downloading the recordings.
  
- **`video_id` folders**: Each folder is named after the YouTube video ID, and inside these folders, you will find:
  
  - **Transcripts**: A `.json` file containing word-by-word transcriptions with corresponding word timestamps.
  
  - **Speaker Timestamps**: A `.csv` file that contains speaker labels and timestamps for each audio segment, indicating when a given speaker is active.
  
  - **`speakers_info.csv`**: A file that contains the diagnosis label (PD or control) and other relevant speaker information.

### Downloading Audio Files

After downloading the Zenodo repository, you can download the audio files for each speaker using the provided script. The script takes the root Zenodo directory as a parameter, which contains the metadata files with YouTube links. To download the audio files inside each speaker's folder, follow these steps:

1. Navigate to the project directory.
2. Run the following script, specifying the root directory of the Zenodo dataset:

```bash
python data/download/download_audios.py --root_dir path_to_zenodo_directory
```

This script will use the `metadata.csv` files in each speaker’s folder to download the corresponding YouTube videos as audio files.

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

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter issues, please open an issue or submit a pull request. Refer to the `CONTRIBUTING.md` file for detailed guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Data Sources:** Acknowledge sources of data and contributions.
- **Funding:** Mention any grants or funding sources if applicable.

## Contact

For questions or further information, please contact [Anna Favaro](mailto:afavaro1@jhu.edu).
