import os
import subprocess
import pandas as pd
from urllib.parse import urlparse, parse_qs

# Path to the metadata file
metadata_file_path = '/export/fs06/afavaro/parkceleb_zenodo/anonym_trial/PD/pd_37/metadata.xlsx'  # Update with your path
# Base path for storing downloaded files
base_output_path = '/export/fs06/afavaro/parkceleb_zenodo/anonym_trial/PD/'
# Function to extract video ID from YouTube URL
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

# Read the metadata file and process each entry
def process_metadata(metadata_file_path):
    df = pd.read_excel(metadata_file_path)  # or pd.read_csv(metadata_file_path) if CSV

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        youtube_url = row.get('LINK')

        if pd.notna(youtube_url):
            video_id = extract_video_id(youtube_url)
            if video_id:
                download_youtube_content(video_id, youtube_url)
            else:
                print(f"Video ID could not be extracted from {youtube_url}")


if __name__ == "__main__":
    process_metadata(metadata_file_path)
