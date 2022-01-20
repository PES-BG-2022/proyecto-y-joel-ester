#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ester, joel

"""
import time


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


n = int(input("Ingresa un número entero "))

combinaciones2 = [[],[]]
combinaciones3 = [[],[]]

primos = primes_upto(n)

    
if n%2 == 0:
    print("Combinación de dos primos:")
    combi2 = 0
    combinaciones2[0].append(n)
    completa = [] 
    for j in primos:
        for k in primos:
            if j + k == n and j*k not in completa:
                combi2 = combi2 + 1
                completa.append(j*k)
                print(j, " + ", k, " = ", n)

    combinaciones2[1].append(combi2)

if n > 5:
    print("Combinación de tres primos:")
    combi3 = 0
    combinaciones3[0].append(n)
    completa = []
    for x in primos:
        for y in primos:
            for z in primos:
                if (x + y + z == n) and x*y*z not in completa:
                    combi3 = combi3 + 1
                    completa.append(x*y*z)
                    print(x, " + ", y, " + ", z, " = ", n)
    
    combinaciones3[1].append(combi3)
   
    
print()
print("Combinaciones para ", n)
print("Suma de dos primos: ", combinaciones2[1], ", Suma de tres primos: ", combinaciones3[1])



        
    

#Todo número par mayor que 2 puede escribirse como suma de dos números primos. 
#Todo número entero mayor que 5 se puede escribir como suma de tres números primos.



