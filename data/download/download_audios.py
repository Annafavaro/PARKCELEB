import os
import sys
import subprocess
import pandas as pd
from urllib.parse import urlparse, parse_qs

def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    video_id = parse_qs(parsed_url.query).get('v')
    if video_id:
        return video_id[0]
    return None

# Function to download audio from YouTube
def download_youtube_content(base_output_path, video_id, youtube_url):
    # Define the output directory for this video ID
    output_dir = os.path.join(base_output_path, video_id)
    os.makedirs(output_dir, exist_ok=True)

    # Define the yt-dlp command
    yt_dlp_command = [
        'yt-dlp', '--retries', '5', '--no-check-certificate',
        '--extract-audio', '--audio-format', 'wav',
        '--output-na-placeholder', 'not_available',
        '-o', os.path.join(output_dir, '%(id)s.%(ext)s'),
        youtube_url
    ]

    # Run the command
    try:
        subprocess.run(yt_dlp_command, check=True)
        print(f"Downloaded and processed: {youtube_url}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {youtube_url}: {e}")

# Function to process metadata files in a given directory
def process_metadata_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('metadata.xlsx'):
                metadata_file_path = os.path.join(root, file)
                print(f"Processing metadata file: {metadata_file_path}")

                # Determine the speaker_id as the part of the path before 'metadata.xlsx'
                parts = metadata_file_path.split('/')
                metadata_index = parts.index('metadata.xlsx')
                speaker_id = parts[metadata_index - 1]
                print(f"Speaker ID: {speaker_id}")

                # Define base output path for this speaker
                base_output_path = os.path.join(directory, speaker_id)

                df = pd.read_excel(metadata_file_path)
                links = df['link'].tolist()

                for link in links:
                    video_id = extract_video_id(link)
                    if video_id:
                        # Define the output directory for this video ID
                        output_dir = os.path.join(base_output_path, video_id)
                        print(f"Output Directory: {output_dir}")
                        if not os.path.exists(output_dir):
                            os.makedirs(output_dir)
                        download_youtube_content(base_output_path, video_id, link)
                    else:
                        print(f"Video ID could not be extracted from {link}")

# Main script execution
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_directory = sys.argv[1] #/export/fs06/afavaro/parkceleb_zenodo/anonym_trial/

    # Directories to traverse
    subdirectories = ['PD', 'CN']
    for subdir in subdirectories:
        subdir_path = os.path.join(root_directory, subdir)
        if os.path.exists(subdir_path):
            process_metadata_files(subdir_path)
        else:
            print(f"Directory does not exist: {subdir_path}")
