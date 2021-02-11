#!/usr/bin/env phython3
"""
"""


from mpi4py import MPI

comn = MPI.COMM_WORLD
size=conm.Get_size()
rank=conm.Get_rank()
name=MPI.Get_processor_name()

head = 0

if rank == head;
	data =" the root process, here some data: "
else:
	data = None

data = comn.bcast(data, root=0)

print (data, rank)


