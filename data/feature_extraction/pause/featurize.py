#!/home/afavaro/new_conda/envs/digypsy
import os
import pandas as pd
import sys

from prosody import Voice_Prosody
import soundfile as sf
from tqdm import tqdm

'''
Featurize Wrapper for grabbing prosody features for audio stored in a folder
'''
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

def main_pause(audio, output_path, fsize=20):
    """
    Featurize Wrapper for grabbing prosody features for audio stored in a folder
    """

    df_list = []  # List to store DataFrames
    vp = Voice_Prosody()
    all_audios = read_audio_files(audio)

    for fi in tqdm(all_audios, desc='featurizing'):
        if '.wav' in fi:
            #print('Featurizing:', fi)
            feat_dict = vp.featurize_audio(fi, int(fsize))
            # Ensure feat_dict is not empty
            if feat_dict:
                df_list.append(pd.DataFrame(feat_dict, index=[0]))  # Convert dict to DataFrame and append
    if df_list:  # Check if there are DataFrames in the list
        df = pd.concat(df_list, ignore_index=True)  # Concatenate DataFrames
       # date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    if output_path:
        df.to_csv(os.path.join(output_path, 'pause' + '.csv'))
        return df
        print("Pause CSV saved")
    else:
        return df
        print("Pause features extracted")
