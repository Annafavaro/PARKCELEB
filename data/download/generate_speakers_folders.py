import wave
import os
import pandas as pd
from pydub import AudioSegment
import sys
def process_audio_files(root_directory):
    """
        This function processes audio files and their corresponding CSV files that contain speaker timestamps.
        It performs the following steps:

        1. Reads the CSV files in the specified directory.
        2. For each CSV, extracts segments of the corresponding audio file based on the start and end times for each speaker.
        3. Saves the audio segments into separate folders for each speaker.
        4. Optionally, concatenates all the segments for a given speaker into a single audio file.

        Parameters:
        - root_directory: The root directory containing the audio files and corresponding CSV files with speaker timestamps.
        """

    all_files = []
    for path, subdirs, files in os.walk(root_directory):
        print(subdirs)
        for name in files:
            if name.endswith(".csv"):
                if "general" not in name and "speaker" not in name and "gecko" not in name:
                    all_files.append(os.path.join(path, name))

    print("Total files to process:", all_files)

    for file in all_files:
        print(f"Processing file: {file}")
        cd = os.path.split(file)[0]
        base_name = os.path.basename(file).split(".csv")[0]
        df = pd.read_csv(file)
        audio_path = os.path.join(cd, base_name + ".wav")

        if not os.path.exists(audio_path):
            print(f"Audio file does not exist: {audio_path}")
            continue

        read_audio = AudioSegment.from_wav(audio_path)
        speakers = list(set(df['speaker'].tolist()))

        for speaker in speakers:
            path_sp = os.path.join(cd, speaker)
            if not os.path.isdir(path_sp):
                print(f"Creating directory: {path_sp}")
                os.makedirs(path_sp)

            speaker_data = df[df['speaker'] == speaker]
            start_times = speaker_data['start'].tolist()
            end_times = speaker_data['end'].tolist()
            timestamps = zip(start_times, end_times)

            for start, end in timestamps:
                start_ms = start * 1000
                end_ms = end * 1000
                print(f"Splitting at [{start_ms}:{end_ms}] ms")
                audio_chunk = read_audio[start_ms:end_ms]
                chunk_path = os.path.join(path_sp, f"{end}.wav")
                audio_chunk.export(chunk_path, format="wav")

            # Concatenate all chunks
            chunk_files = [f for f in os.listdir(path_sp) if f.endswith(".wav")]
            chunk_files.sort(key=lambda x: float(x.split(".wav")[0]))
            sorted_chunk_paths = [os.path.join(path_sp, f) for f in chunk_files]

            if sorted_chunk_paths:
                outfile = os.path.join(path_sp, "recording_concatenated.wav")
                data = []
                for chunk_path in sorted_chunk_paths:
                    with wave.open(chunk_path, 'rb') as w:
                        data.append([w.getparams(), w.readframes(w.getnframes())])

                with wave.open(outfile, 'wb') as output:
                    output.setparams(data[0][0])
                    for params, frames in data:
                        output.writeframes(frames)

                print(f"Concatenated audio saved: {outfile}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_directory = sys.argv[1]
    process_audio_files(root_directory)
