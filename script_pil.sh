#!/bin/bash

#SBATCH --job-name=pil_image
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=ibm_small
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=1
#SBATCH --output=output_pil.out
#SBATCH --error=error_pil.err

source /home/terminal29/venv38/bin/activate

module load mpi/openmpi/3.0.0

mpiexec -np 1 python3 pil_image.py