import os
import subprocess
import pandas as pd
from urllib.parse import urlparse, parse_qs

# Root directories for PD and CN
root_directories = [
    '/export/fs06/afavaro/parkceleb_zenodo/anonym_trial/PD/',
  #  '/export/fs06/afavaro/parkceleb_zenodo/anonym_trial/CN/'
]

def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    video_id = parse_qs(parsed_url.query).get('v')
    if video_id:
        return video_id[0]
    return None

# Function to download audio from YouTube
def download_youtube_content(video_id, youtube_url):
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
            print(file)
            if file.endswith('metadata.xlsx'):
                metadata_file_path = os.path.join(root, file)
                print(f"Processing metadata file: {metadata_file_path}")
                df = pd.read_excel(metadata_file_path)  # or pd.read_csv(metadata_file_path) if CSV
                links = df['link'].tolist()
                for link in links:
                    video_id = extract_video_id(link)
                    if video_id:
                        # Define the base path for storing downloaded files
                        base_output_path = os.path.join(directory, video_id)
                        # Check if directory already exists
                        if not os.path.exists(base_output_path):
                            os.makedirs(base_output_path)
                        download_youtube_content(video_id, link)
                    else:
                        print(f"Video ID could not be extracted from {link}")

# Process all metadata files in PD and CN directories
for root_directory in root_directories:
    process_metadata_files(root_directory)

if __name__ == "__main__":
    for root_directory in root_directories:
        process_metadata_files(root_directory)
