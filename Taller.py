import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

current = os.getcwd()
file = glob.glob(current+'/*.csv')
mmse =pd.read_csv(file[0],sep=';')

print(mmse['Edad en la visita'])

ordenado=mmse.sort_values(by='Edad en la visita')
mmse_ordenado = ordenado.reset_index(drop= True)

print(mmse_ordenado)
