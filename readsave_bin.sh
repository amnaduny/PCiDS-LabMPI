#!/bin/bash

#SBATCH --job-name=readsave_bin
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=2
#SBATCH --partition=ibm_small
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=4
#SBATCH --output=readsave_bin.out
#SBATCH --error=readsave_bin.err

source /home/terminal29/venv38/bin/activate

python3 readsave_bin.py