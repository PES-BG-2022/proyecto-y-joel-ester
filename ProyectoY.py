#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 20:14:28 2022

@author: ester
"""

#Todo número par mayor que 2 puede escribirse como suma de dos números primos. 
#Todo número entero mayor que 5 se puede escribir como suma de tres números primos.


import time
import pandas as pd
import numpy as np

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
    print('ya calcule los primos')
    return primos


n = 200

combinaciones2 = [[],[]]
combinaciones3 = [[],[]]

inicio = time.time()

lista_primos = primes_upto(n)


for i in range(3, n+1):
    primos =  np.array(lista_primos)
    primos = primos[primos<i]
    
    if i%2 == 0:
        combi2 = 0
        combinaciones2[0].append(i)
        completa = []
        for j in primos:
            for k in primos:
                if j + k == i and j*k not in completa:
                    combi2 = combi2 + 1
                    completa.append(j*k)
        
        combinaciones2[1].append(combi2)
    
    if i > 5:
        combi3 = 0
        combinaciones3[0].append(i)
        completa = []
        for x in primos:
            for y in primos:
                for z in primos:
                    if (x + y + z == i) and x*y*z not in completa:
                        combi3 = combi3 + 1
                        completa.append(x*y*z)
        
        combinaciones3[1].append(combi3)
        
    if i%100 == 0:
        df2 = pd.DataFrame(combinaciones2).T
        df3 = pd.DataFrame(combinaciones3).T
        
        df2.to_csv('Cambinaciones2.csv', index = False, 
                   header =['n','combinaciones'])
        df3.to_csv('Cambinaciones3.csv', index = False,
                   header =['n','combinaciones']) 
        
        print("me voy a morir wuuuuu:  ", i)
        

final = time.time()-inicio                
print(final)



       



