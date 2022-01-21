#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:03:57 2022

@author: ester
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("combinaciones_g2.csv")

sns.set(rc = {'figure.figsize':(15,8)})
sns.set_style("whitegrid")
graf2 = sns.scatterplot(data=df, x="n", y="combinaciones", marker="+", palette="grey")

graf2.grid(False)
graf2.set_ylabel("Cantidad de combinaciones de la suma de 2 primos")
graf2.set_xlabel("Número entero")

plt.savefig('dos-combinaciones.pdf')
plt.show()

df2 = pd.read_csv("Cambinaciones3.csv")

sns.set(rc = {'figure.figsize':(15,8)})
sns.set_style("whitegrid")
graf3 = sns.scatterplot(data=df2, x="n", y="combinaciones", marker="+", palette="grey")

graf3.grid(False)
graf3.set_ylabel("Cantidad de combinaciones de la suma de 3 primos")
graf3.set_xlabel("Número entero")

plt.savefig('tres-combinaciones.pdf')