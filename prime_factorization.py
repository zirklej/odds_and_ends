# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:16:13 2016

@author: joelz
"""

'''prime factorization using primes.txt'

'''

def prime_factorization(x):
    prime_factor=dict()
    fin=open('primes.txt')
    #print(fin.readline())   
    while x!=1:
        prime_counter=0
        p=int(fin.readline())
        #print(p)
        while x%p==0:
            prime_counter+=1
            x=x/p
        if prime_counter!=0:
            prime_factor[p]=prime_counter
    fin.close()
    return prime_factor
      
#print(prime_factorization(2))
            

    

