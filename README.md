# :star: :dizzy: PARKCELEB :star: :dizzy:

## Overview 

This study explores innovative methods for detecting Parkinson’s disease (PD) through speech analysis, addressing limitations in existing datasets, which often lack prodromal recordings and longitudinal data. 
To overcome these gaps, we created ParkCeleb, a novel speech corpus containing recordings from 40 celebrities with PD and 40 control subjects. The dataset spans ten years before to twenty years after diagnosis, providing a comprehensive view of evolving speech characteristics.

## Objectives

- **Create ParkCeleb Corpus:** Develop a comprehensive corpus of longitudinal speech recordings from subjects with PD and CNs.
- **Feature Extraction and Analysis:** Analyze the temporal evolution of speech features such as pitch variability, pause duration, speech rate, and syllable duration.
- **Model Evaluation:** Assess the effectiveness of machine learning models in PD detection using data from prodromal and post-diagnosis phases.

## ParkCeleb

The **ParkCeleb** data set is stored in the following [Zenodo repository](link). This repo does not contain the actual audio recordings but provides metadata files with links to YouTube videos, speaker information, and transcriptions. Below is an explanation of the folder structure and how to work with the provided files to download and process the data.

## Directory Structure

### Root Directory

The root directory contains two main subdirectories:

- **PD**: Speech data of celebrities diagnosed with Parkinson’s disease.
- **CN**: Speech data of control subjects.

Inside the root directory, you will also find the following key files:

- **speakers_pairs.xlsx**: Contains the pairs of speakers (PD-CN) gender and age-matched used in the classification and longitudinal analysis.
- **PD_demo.xlsx**: A metadata file with demographic information related to the PD group.
- **CN_demo.xlsx**: A metadata file with demographic information related to the CN group.

### Speaker Folders

Each speaker is assigned an anonymized folder labeled by their ID, e.g., `cn_xx` for control subjects or `pd_xx` for PD subjects, where `xx` is a number ranging from 01 to 40. Inside each speaker’s folder, you will find a `metadata.csv` file containing YouTube video links for downloading the corresponding recordings.

Each speaker folder also includes subfolders named after the YouTube video ID. Inside these video-specific subfolders, you will find:

- **Transcription File (.json)**: Contains word-by-word transcriptions with corresponding timestamps for each word.
- **Speaker Timestamps File (.csv)**: Contains speaker labels and timestamps, indicating when each speaker is active during the recording.
- **Target Speaker Annotation (speakers_info.csv)**:
  - **Column status**: Identifies the target speaker in the video (whether they are the PD or CN subject).
  - **Column years_from_diagnosis**: Specifies how many years before or after diagnosis the recording occurred.

For control subjects (CNs), the timeline is matched to the diagnosis year of the corresponding PD subject for comparative purposes.

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
   git clone https://github.com/Annafavaro/PARKCELEB.git](https://github.com/Annafavaro/PARKCELEB.git
   cd PARKCELEB
   ```

2. **Install Dependencies:**

   Create a virtual environment and install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Extract Features:**

   The scripts to extract the acoustic interpretable and non-interpretable features are located in:

   ```
   PARKCELEB/features/interpretable_features 
   ```

   ```
   PARKCELEB/features/non_interpretable_features
   ```
## Citing ParkCeleb
If you use ParkCeleb in your research, please cite the following publication:

```bibtex
@article{},
  title={},
  author={}
}
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
