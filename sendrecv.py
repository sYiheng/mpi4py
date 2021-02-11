#!/usr/bin/env python3
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
data = []

# Point-to-Point Communication (p2p)
if rank == 0:
	data.append(rank)
	comm.send(data,dest = (rank+1)%size) # From rank 0 send it to the next rank
if rank > 0:
	message = comm.recv(source = (rank - 1)%size) # Get the data from previousn rank
	data.append(rank)
	comm.send(data,dest = (rank+1)%size) # And send it to the next rank
	# The '%size' makes sure that only ints between 0~(size-1) will be passed to dest
if rank == 0:
	message = comm.recv(source=size -1) # Receive from the last rank
	print("The end")	


print("I received:", message, "from :", rank)
