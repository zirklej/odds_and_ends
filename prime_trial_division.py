# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 18:27:33 2016

@author: joelz
"""

'''Trial Division

Find the first 50000 (~) primes and write them to a file for future use.

'''
import math

fout=open('primes.txt','a')
#fout.write('2\n')
#fout.write('3\n')

for i in range(100001,333334):
    #use only 3k+1 or 3k-1
    down=3*i-1
    up=3*i+1
    #print(i)
    for j in range(2,int(math.ceil(math.sqrt(down))+1)):
        if down%j==0:
            break 
        else:
            if j==math.ceil(math.sqrt(down)):
                fout.write(str(down)+'\n')
    for j in range(2,int(math.ceil(math.sqrt(up))+1)):
        if up%j==0:
            break
        else:
            if j==math.ceil(math.sqrt(up)):
                fout.write(str(up)+'\n')

fout.close()