#!/usr/bin/env python3
"""
clusterfs read test......
"""

from mpi4py import MPI
import sys


size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

fpIn = open("/clusterfs/test.txt", "r")

contents = fpIn.read();

print("I am process %d of %d on %s."  % (rank, size, name))
print(contents)
