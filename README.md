# :star: :dizzy: PARKCELEB :star: :dizzy:

## Overview 

This work investigates the potential for early detection of Parkinson’s Disease (PD) through a longitudinal analysis of speech recordings from celebrities who publicly disclosed their diagnosis. This corpus includes longitudinal speech data collected from 40 subjects with PD and 40 controls (CNs). By analyzing speech features from 10 years before to 20 years after diagnosis, we aim to uncover patterns indicative of early PD progression.

## Objectives

- **Create ParkCeleb Corpus:** Develop a comprehensive corpus of longitudinal speech recordings from subjects with PD and CNs.
- **Feature Extraction and Analysis:** Analyze the temporal evolution of speech features such as pitch variability, pause duration, speech rate, and syllable duration.
- **Model Evaluation:** Assess the effectiveness of machine learning models in PD detection using data from prodromal and post-diagnosis phases.

## ParkCeleb

The **ParkCeleb** data set is stored in the following [Zenodo repository](link). This repo does not contain the actual audio recordings but provides metadata files with links to YouTube videos, speaker information, and transcriptions. Below is an explanation of the folder structure and how to work with the provided files to download and process the data.

### Folder Structure

The main directory has two directories, one for the PD group and one for the CN group. Inside this directory, you will also find:

- **`speakers_pairs.xlsx`**: A file containing the paired speakers (CN-PD) for classification and longitudinal analysis.
- **`PD_demo.xlsx`**: A file containing the metadata for the PD group.
- **`CN_demo.xlsx`**: A file containing the metadata for the CN group.

Each speaker has an anonymized folder named after their ID (e.g., `cn_01` for controls or `pd_01` for Parkinson’s Disease subjects). Inside each speaker's folder, you will find:

- **`metadata.csv`**: A file containing YouTube video links for downloading the recordings.
  
- **`video_id` folders**: Each folder is named after the YouTube video ID, and inside these folders, you will find:
  
  - **Transcripts**: A `.json` file containing word-by-word transcriptions with corresponding word timestamps.
  
  - **Speaker Timestamps**: A `.csv` file that contains speaker labels and timestamps for each audio segment, indicating when a given speaker is active.
  
  - **`speakers_info.csv`**: A file that contains the diagnosis label (`target` for PD and `non-target` for CN) and indication about how many years before or after diagnosis the video was recorded. Note that this indication was provided for both PD and CNs. In the case of the CN group, the year from diagnosis refers to the year of diagnosis of the matched PD subject.

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
