import json
import os
import whisperx

def process_audio_files(root_directory, hf_token, device="cuda", batch_size=16, compute_type="float16"):
    """
    Processes audio files in the specified root directory using WhisperX for transcription, alignment, and diarization.

    Parameters:
    - root_directory (str): The root directory containing audio files and metadata files.
    - hf_token (str): The Hugging Face token for accessing the diarization model.
    - device (str): The device to run the model on, such as 'cuda' or 'cpu'. Default is 'cuda'.
    - batch_size (int): The batch size for processing audio. Default is 16.
    - compute_type (str): The type of computation for the model, such as 'float16'. Default is 'float16'.

    Outputs:
    - CSV files: Speaker diarization results saved as CSV files in the same directory as the audio file.
    - JSON files: Transcription results, including alignment and speaker labels, saved as JSON files in the same directory as the audio file.
    """

    # Load Whisper model
    model = whisperx.load_model("medium", device, compute_type=compute_type)

    # Find all audio files
    all_files_audio = []
    for path, subdirs, files in os.walk(root_directory):
        for name in files:
            if name.endswith("wav"):
                all_files_audio.append(os.path.join(path, name))
    print(f"Found {len(all_files_audio)} audio files.")

    # Find all CSV files that do not have 'speakers_info' or 'gecko' in the name
    all_files_csv = []
    for path, subdirs, files in os.walk(root_directory):
        for name in files:
            if name.endswith(".csv") and "speakers_info" not in name and "gecko" not in name:
                base = os.path.join(path, name.split(".csv")[0])
                all_files_csv.append(base + ".wav")
    print(f"Found {len(all_files_csv)} CSV files.")

    # Discard audios already diarized
    total_files = [i for i in all_files_audio if i not in all_files_csv]
    print(f"Processing {len(total_files)} new audio files.")

    for audio_file in total_files:
        dir = os.path.split(audio_file)[0]
        base_name = os.path.basename(audio_file).split(".wav")[0]
        print(f"Processing file: {base_name}")

        # Define paths for CSV and JSON files
        csv_path = os.path.join(dir, base_name + ".csv")
        json_path = os.path.join(dir, base_name + ".json")

        # Transcribe audio
        audio = whisperx.load_audio(audio_file)
        result = model.transcribe(audio, batch_size=batch_size)

        # Align transcription
        model_a, metadata = whisperx.load_align_model(language_code='en', device=device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

        # Perform diarization
        diarize_model = whisperx.DiarizationPipeline(use_auth_token=hf_token, device=device)
        diarize_segments = diarize_model(audio_file)
        result = whisperx.assign_word_speakers(diarize_segments, result)

        # Save results
        diarize_segments.to_csv(csv_path)
        with open(json_path, "w") as outfile:
            json.dump(result, outfile)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python process_audio.py <root_directory>")
        sys.exit(1)

    root_directory = sys.argv[1]
    YOUR_HF_TOKEN = '<YOUR_HF_TOKEN>'
    process_audio_files(root_directory, YOUR_HF_TOKEN)
