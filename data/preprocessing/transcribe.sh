#!/bin/bash -l
#SBATCH --time=10:0:0
#SBATCH --partition=gpu-a100
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=100G
#SBATCH --gres=gpu:1
#SBATCH --account=a100acct

source  activate whisper_new
ml purge
#module load namd/2.14-cuda-smp
module load cuda/11.7
ml
nvidia-smi
export CUDA_VISIBLE_DEVICES=0,1,2,3
export CONV_RSH=ssh

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/before/ten_years/CN/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/before/ten_years/CN/

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/before/ten_years/PD/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/before/ten_years/PD/

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/before/five_years/PD/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/before/five_years/PD/

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/before/five_years/CN/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/before/five_years/CN/

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/after/five_years/PD/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/after/five_years/PD/

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/after/five_years/CN/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/after/five_years/CN/

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/after/ten_years/CN/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/after/ten_years/CN/

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/after/ten_years/PD/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/after/ten_years/PD/

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/after/ten_years_above/CN/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/after/ten_years_above/CN/

python /export/b16/afavaro/youtube/Experiments/Transcribe/transcribe.py /export/c01/afavaro/ParkCeleb_submission/data/after/ten_years_above/PD/\
 /export/c01/afavaro/ParkCeleb_submission/data_transcripts/after/ten_years_above/PD/
