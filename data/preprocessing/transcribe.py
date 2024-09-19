# conda activate whisper_new
import sys
import os
import whisper
import torch
from tqdm import tqdm

if torch.cuda.is_available():
    print(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. Using CPU.")
model = whisper.load_model("medium", device="cuda")
limit_mb = 25


def main(root, output_path, limit_mb=25):
    """
    Transcribe audio files in a directory tree and save transcripts as text files.

    Args:
    - root (str): Root directory containing audio files.
    - output_path (str): Output directory to save transcripts.
    - limit_mb (int, optional): Maximum file size in MB for transcription. Default is 25.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Get base names of existing transcripts
    existing_transcripts = {os.path.splitext(f)[0] for f in os.listdir(output_path) if f.endswith('.txt')}

    # Collect all .wav files to process
    audio_files = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name.endswith('.wav') and 'concat' not in name:
                audio_files.append((path, name))

    # Process files with a progress bar
    for path, name in tqdm(audio_files, desc="Transcribing audio files"):
        base_name = os.path.basename(name).split(".wav")[0]
        if base_name in existing_transcripts:
            print(f"Skipping {name} as transcript already exists.")
            continue
        audio_file = os.path.join(path, name)
        file_size_bytes = os.path.getsize(audio_file)
        file_size_mb = file_size_bytes / (1024 * 1024)
        # if file_size_mb <= limit_mb:
        out_path_file = os.path.join(output_path, base_name + '.txt')
        try:
            with open(out_path_file, 'w') as output:
                out = model.transcribe(audio_file, language="en")
                transcript = out['text']
                output.write(transcript)
        except Exception as e:
            print(f"Error processing file '{audio_file}': {e}")


if __name__ == "__main__":
    root = sys.argv[1]
    output_path = sys.argv[2]
    main(root, output_path)
