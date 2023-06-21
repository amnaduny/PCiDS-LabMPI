#!/usr/bin/bash

#SBATCH --job-name=mpi_image
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --partition=ibm_small
#SBATCH --time=00:10:00
#SBATCH --output=mpi_image.out
#SBATCH --error=mpi_image.err

source /home/terminal29/venv38/bin/activate

module load mpi/openmpi/3.0.0

mpiexec -np 1 python3 mpi_image.py
