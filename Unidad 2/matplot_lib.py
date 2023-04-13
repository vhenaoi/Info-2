import matplotlib.pyplot as plt
import numpy as np

#fig, ax = plt.subplots()
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
#ax.plot([1, 2, 2, 4], [1, 1, 2, 2])
#ax.set_ylabel('Amplitud')
#ax.set_xlabel('Tiempo')
#plt.show()

plt.plot(np.random.rand(10),np.random.rand(10),color='#617AED',marker='o',linestyle='--',label='Linea 1')
plt.plot(np.random.rand(10), np.random.rand(10),color='#D4A357',label='Linea 2')
plt.scatter(np.random.rand(10), np.random.rand(10),color='#F65165',label='puntos')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo')
plt.grid()
plt.legend()
plt.show()