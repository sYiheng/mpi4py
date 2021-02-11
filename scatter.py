#! /usr/bin/env python3
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
data = []
root = 0

# Scatter
if rank == 0:
	# Create a list of random integers with length 'size'
	m = np.random.randint(0,size,size=size) 
	print("message: ", m)
	data = m

send = comm.scatter(data, root) # Get the data from root and scatter it to every processor
print("Rank ", rank, " received: ",send) 
