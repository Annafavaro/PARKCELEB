# 💫 Unveiling Early Signs of Parkinson’s Disease via a Longitudinal Analysis of Celebrity Speech Recordings 💫 

## Overview 📈

This study explores innovative methods for detecting Parkinson’s disease (PD) through speech analysis, addressing limitations in existing pathological speech corpora, which often lack prodromal recordings and longitudinal data. 
We created *ParkCeleb*, a novel speech corpus containing recordings from 40 celebrities with PD and 40 control subjects to overcome these gaps. The dataset spans ten years before to twenty years after diagnosis, providing a comprehensive view of evolving speech signs associated to PD.

### 🎙️ ParkCeleb 🎙️

The **ParkCeleb** data set is stored in the following [Zenodo repository](https://zenodo.org/uploads/13954768). This repository does not contain the actual audio recordings but provides metadata files with links to YouTube videos, speaker information, and transcriptions. 
The current GitHub repository is used to download audio files for each speaker, segment the recordings using provided scripts, and extract both interpretable and non-interpretable features. The scripts organize the audio into speaker-specific folders and extract relevant audio segments based on timestamps.
## 1. Installation️ 💻 

To set up the project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Annafavaro/PARKCELEB.git](https://github.com/Annafavaro/PARKCELEB.git
   cd PARKCELEB
   ```

2. **Install Dependencies** 

   Create a virtual environment and install the required packages:

   ```bash
   pip install -r requirements2.txt
   ```
## 2. Get Audio Files 🎧🎵

   After downloading the Zenodo repository, you can download the audio files for each speaker using the provided script. The script takes the root Zenodo directory as a parameter, which contains the metadata files with YouTube links. To download the audio files inside each speaker's folder, follow these steps:

   1. Navigate to the project directory.
   2. Run the command below, specifying the root directory of the Zenodo dataset. This script will use the `metadata.csv` files in each speaker’s folder to download the corresponding YouTube videos as audio files.
   ```bash
   python data/download/download_audios.py --root_dir path_to_zenodo_directory
   ```
   3. For each speaker found in the CSV file containing speaker timestamps for each video, the script ***generate_speakers_folders.py*** creates a separate directory named after the speaker (e.g., SPEAKER_OO). Inside each speaker's directory, the script saves individual audio segments that correspond to the start and end times specified in the CSV file. These segments are saved as .wav files, with the filename corresponding to the end time of the segment (e.g., 12345.wav).
   To generate separate audio directories for each speaker recorded in a given video, run the following command:
   ```bash
   python data/download/generate_speakers_folders.py --root_dir path_to_zenodo_directory
   ```

   4. Extract Features

   The scripts to extract the acoustic interpretable and non-interpretable features are located in:

   ```
   /features/interpretable_features/
   ```

   ```
   /features/non_interpretable_features/
   ```

## ⚠️ Important Note on Video Availability  

Please be aware that some YouTube videos referenced in the **ParkCeleb** metadata may no longer be available, as they have been removed or restricted since the dataset's creation. At the time of compiling **ParkCeleb**, all linked videos were accessible.  

To ensure the quality and consistency of the dataset, we:  
- **Included only audio segments longer than 8 seconds**, as shorter segments were found to reduce diarization precision.  
- **Balanced the dataset**, ensuring an equal number of recordings for subjects with Parkinson’s Disease (PD) and control subjects.  

## Citing ParkCeleb 📖
If you use ParkCeleb in your research, please cite the following publication:

```bibtex
@article{favaro2024unveiling,
  title={Unveiling early signs of Parkinson’s disease via a longitudinal analysis of celebrity speech recordings},
  author={Favaro, Anna and Butala, Ankur and Thebaud, Thomas and Villalba, Jes{\'u}s and Dehak, Najim and Moro-Vel{\'a}zquez, Laureano},
  journal={npj Parkinson's Disease},
  volume={10},
  number={1},
  pages={207},
  year={2024},
  publisher={Nature Publishing Group UK London}
}
```

## Contributing 👭🏻

Contributions are welcome! If you have suggestions for improvements or encounter issues, please open an issue or submit a pull request. Refer to the `CONTRIBUTING.md` file for detailed guidelines.

## License 🪪

This project is licensed under the MIT License.

## Acknowledgments 🛜

- **Data Sources:** The speech data used in this study was sourced from publicly available YouTube videos of celebrities with and without PD. Those with PD voluntarily disclosed their diagnosis in public.
- **Funding:** This work was partly funded by the Richman Family Precision Medicine Center of Excellence—Venture Discovery Fund and Consolidated Anti-Aging Foundation. The study sponsors did not have any role in the study design, in the collection, analysis, and interpretation of data, in the writing of the manuscript, and in the decision to submit the manuscript for publication.

## Contact 📱

For questions or further information, please contact [Anna Favaro](mailto:afavaro1@jhu.edu).
