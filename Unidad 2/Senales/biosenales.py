# %%
#PRIMER PUNTO

#libreria de entrada salida de datos
import scipy.io as sio
#transforamda rapida de fourier, para cuantificar las oscilaciones
from scipy import stats
#manejo de tensores ndarray
import numpy as np
#graficar
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import cv2

#estoy cargando unos datos que fueron previamente recolectados
#usamos el sio para cargar los datos
path = r'E:\Academico\Universidad\Cursos\Repositorios\Info-2\Senales\C001R_EP_reposo.mat'
mat_contents = sio.loadmat(path) 
print('La variable cargada es del tipo: ' + str(type(mat_contents))) 
print('las llaves son: ' + str(mat_contents.keys())) 

senal = mat_contents['data'] 
print("dimensión: ",senal.ndim) 
print("Forma: ",senal.shape) 

#COMO HACEMOS CONTINUA
sensores = senal.shape[0] 
puntos = senal.shape[1] 
epocas = senal.shape[2] 

#reshape(senal_original, forma_nueva)
senal_continua = np.reshape(senal,(sensores,puntos*epocas),order = 'F') 
print(senal_continua.shape) 

pd_senal=pd.DataFrame(senal_continua)
promedio=pd_senal.apply(lambda x : x.mean(), axis=1, args=())
mediana=pd_senal.apply(lambda x : x.median(), axis=1, args=())
moda=pd_senal.apply(lambda x : stats.mode(x), axis=1, args=())
sns.kdeplot(promedio)
new_pd_senal = pd.DataFrame()
new_pd_senal['signal1'] = senal[0,:,0]

df = pd.DataFrame(senal[0,:100,:-100])
hm = sns.heatmap(df, cmap="YlGnBu")
plt.show()
img=cv2.imread(r"C:\Users\veroh\Downloads\Figure_1.png")
imgR=img[:,:,0]
cv2.namedWindow('Ventana',0)
cv2.imshow('Ventana',imgR)

#graficamos
plt.subplot(1,2,1) 
plt.plot(senal[0,:,0]) 

plt.subplot(1,2,2) 
plt.plot(senal_continua[0,0:1999]) 

plt.show() 









