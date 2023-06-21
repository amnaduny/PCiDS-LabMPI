#!/bin/bash

#SBATCH --job-name=pil_image
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=4
#SBATCH --partition=ibm_small
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=1
#SBATCH --output=mpi3.out
#SBATCH --error=mpi3.err

source /home/terminal29/venv38/bin/activate

module load mpi/openmpi/3.0.0

mpiexec -np 12 python3 mpi3.py