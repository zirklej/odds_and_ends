# -*- coding: utf-8 -*-
"""
Created on Wed Oct 03 17:59:07 2018

@author: zirklej
"""
from numpy import *

# interger to be partitioned
N=20

# largest integer to be included in partition
n=4

def check_sum(x):
    # initialize index array for holding indices of rows when sum>20
    indices=array([])
    for i in range(size(x,0)):
        if sum(x[i,:])<=20: # keep
            pass
        else:
            indices=append(indices,i)
    return delete(x,indices,0)

def append_next_position(i):
    # find index of first zero 
    index=nonzero(i)[0][-1]+1
    # find index of last nonzero
    nnz=index-1
    # next element needs to be <= last nonzero integer
    M=int(i[nnz])
    # create a temp array of size M x 20
    # first row change first zero to M
    # second row change first zero to M-1
    # etc...
    temp=zeros((M,20))
    # put uses indexing according to FLATTENED array
    index_of_flat=index
    next_element=M
    for k in range(size(temp,0)):
        # put i inside temp
        temp[k,:]=i
        put(temp,index_of_flat,next_element)
        index_of_flat+=20
        next_element-=1
    # check that sum of rows in temp array is <=20
    temp=check_sum(temp)
    return temp

# initialize arrays
initial=array([array([i,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) 
                for i in range(1,n+1)])  
# initialize array to hold final partitions
final=zeros(20) 
# initialize counter
counter=0
while len(initial)>0:
    temp=append_next_position(initial[0])
    # delete first element in initial
    initial=delete(initial,0,0)
    # check sums of elements of initial
    # keep track of indices where sum==20
    indices=array([])
    for i in range(len(temp)):
        if sum(temp[i])==20:
            # increment counter and delete element from initial
            indices=append(indices,i)
        else:
            pass
    # delete elements with sums==20 from temp before stacking
    if size(indices)>0:
        indices=indices.astype(int)
        final=vstack((final,temp[indices]))
        temp=delete(temp,indices,0)
    # stack temp on initial
    initial=vstack((initial,temp))
    counter+=len(indices)
    print counter,len(initial)

print counter
final=delete(final,0,0)
    
# print data to file
fin=open("partition.txt","w+")
savetxt(fin,final,fmt='%d')
fin.close()

