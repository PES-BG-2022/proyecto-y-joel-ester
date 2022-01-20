#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ester, joel

"""
import time
import pandas as pd

def primes_upto(x: int):
    primos = []
    for j in range(x+1):
        if j >= 2:
            numeros = []
            for i in range(j+1):
                if i > 0:
                    if j%i == 0:
                        numeros.append(i)
            if len(numeros) == 2:
                primos.append(j)
    return primos


n = 100

combinaciones2 = [[],[]]
combinaciones3 = [[],[]]

primos = primes_upto(n)

    
if n%2 == 0:
    combi2 = 0
    combinaciones2[0].append(n)
    for j in primos:
        for k in primos:
            if j + k == n:
                combi2 = combi2 + 1
                
    if combi2 % 2 != 0:
        combi2 = combi2//2 + 1
        combinaciones2[1].append(combi2)
    else:
        combi2 = combi2/2
        combinaciones2[1].append(combi2)

if n > 5:
    combi3 = 0
    combinaciones3[0].append(n)
    completa = []
    for x in primos:
        for y in primos:
            for z in primos:
                if (x + y + z == n) and x*y*z not in completa:
                    combi3 = combi3 + 1
                    completa.append(x*y*z)
    
    combinaciones3[1].append(combi3)
    

df2 = pd.DataFrame(combinaciones2).T
df3 = pd.DataFrame(combinaciones3).T

df2.to_csv('Cambinaciones2.csv')
df3.to_csv('Cambinaciones3.csv') 
    

        
print(combinaciones2, combinaciones3)



        
    

#Todo número par mayor que 2 puede escribirse como suma de dos números primos. 
#Todo número entero mayor que 5 se puede escribir como suma de tres números primos.



