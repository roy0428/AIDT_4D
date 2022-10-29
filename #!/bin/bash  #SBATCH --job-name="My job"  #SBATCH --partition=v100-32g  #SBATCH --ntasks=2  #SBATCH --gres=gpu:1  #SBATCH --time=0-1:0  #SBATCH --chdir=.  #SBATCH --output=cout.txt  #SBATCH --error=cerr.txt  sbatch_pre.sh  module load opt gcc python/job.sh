#!/bin/bash

#SBATCH --job-name="My job"
#SBATCH --partition=v100-32g
#SBATCH --ntasks=2
#SBATCH --gres=gpu:1
#SBATCH --time=0-1:0
#SBATCH --chdir=.
#SBATCH --output=cout.txt
#SBATCH --error=cerr.txt

module load python/3.9.13-gpu
./AIDT_4D/localization.sh
