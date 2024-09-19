import sys
from speech_rate.feature_extraction_utils import * 
import pandas as pd
import os
import parselmouth
import soundfile as sf
from tqdm import tqdm

def read_audio_files(input_dir):
    """
    Reads all .wav audio files from a directory tree.

    Args:
        input_dir (str): Root directory to search for audio files.

    Returns:
        list: A list of file paths for the audio files.
    """
    all_audios = []
    for path, subdirs, files in os.walk(input_dir):
        for name in files:
            if name.endswith('.wav'):
                file_path = os.path.join(path, name)
                # Check if file size is greater than or equal to 56 bytes
                if os.path.getsize(file_path) >= 56:
                    duration = sf.info(file_path).duration
                    if duration >= 1.0:
                        all_audios.append(file_path)

    return all_audios

def extract_intensity_features(input_path, output_path):
    """
    Extracts intensity, pitch, and formant features from all .wav files in the input directory
    and saves the features to a CSV file.

    Parameters:
        input_path (str): Root directory path where audio files are located.
        output_path (str): Directory path where the output CSV file will be saved.

    Returns:
        pandas.DataFrame: DataFrame containing extracted features.
    """
    all_audios = sorted(read_audio_files(input_path))

    df_tot = []
    failed = False

    for file in all_audios:
        print(file)

        df = pd.DataFrame()
        attributes = {}
        sound = parselmouth.Sound(file)
        sound.scale_intensity(70)  # Scale intensity to a fixed level

        # Extract intensity and pitch features
        intensity_attributes = get_intensity_attributes(sound)[0]
        pitch_attributes = get_pitch_attributes(sound)[0]
        attributes.update(intensity_attributes)
        attributes.update(pitch_attributes)

        # Try to extract formant features
        try:
            formant_attributes = get_formant_attributes(sound)[0]
            attributes.update(formant_attributes)
        except:
            failed = True

        # Add extracted attributes to the DataFrame
        for attribute in attributes:
            df.at[0, attribute] = attributes[attribute]

        df.at[0, 'tot_name'] = file  # Add the file path as an identifier
        rearranged_columns = df.columns.tolist()[-1:] + df.columns.tolist()[:-1]  # Reorder columns
        df = df[rearranged_columns]
        df_tot.append(df)

    if failed:
        print("Failed to compute some formant features.")

    # Concatenate all DataFrames into a single DataFrame
    new_df = pd.concat(df_tot, ignore_index=True)

    # Assign new index names
    new_index_names = ['{}'.format(i) for i in range(1, len(new_df) + 1)]
    new_df.index = new_index_names

    # Save DataFrame to CSV if an output path is provided
    if output_path:
        out_path = os.path.join(output_path, "intensity.csv")
        new_df.to_csv(out_path, index=False)
        return new_df
    else:
        return new_df
