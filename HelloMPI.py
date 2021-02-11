#!/usr/bin/env python3

from mpi4py import MPI
import sys

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

fpIn = open("/clusterfs/test.txt")

contents= fpIn.read()

print("Hello World from %2d of %2d on %s"%(rank, size, name))
print(contents)
