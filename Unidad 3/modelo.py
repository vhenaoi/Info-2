# Trasferencia de datos

import pymongo
import scipy.io as sio
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import cv2

client = pymongo.MongoClient("mongodb+srv://veronicahenaoi:info123@clusterinfo2.8v994es.mongodb.net/?retryWrites=true&w=majority")
db = client.test

class Sistema():
    def __init__(self,client):
        mydb = client["Hospital"]
        self.__neurologia = mydb["neurologia"]
    
    def verificar_db(self,cedula):
        x = self.__neurologia.find_one({'Cédula':int(cedula)})
        if x == None:
            return None, None
        else:
            return x['Nombre'],x['Edad']
    
    def cedula(self,cedula):
        x=self.__neurologia.insert_one({'Cédula':cedula})
    
    def nombre(self,cedula,nombre):
        myquery = {'Cédula':cedula}
        newvalues = { "$set": { "Nombre":nombre} }
        self.__neurologia.update_one(myquery, newvalues) 
    
    def edad(self,cedula,edad):
        myquery = {'Cédula':cedula}
        newvalues = { "$set": { "Edad":edad} }
        self.__neurologia.update_one(myquery, newvalues) 

    def grafica(self,path_signal):
        mat_contents = sio.loadmat(path_signal) 
        senal = mat_contents['data'] 
        sensores = senal.shape[0] 
        puntos = senal.shape[1] 
        epocas = senal.shape[2] 
        senal_continua = np.reshape(senal,(sensores,puntos*epocas),order = 'F') 
        return senal_continua
    
    #def prom(self,senal_continua):
    #    pd_senal=pd.DataFrame(senal_continua)
    #    promedio=pd_senal.apply(lambda x : x.mean(), axis=1, args=()) 
    #    return promedio

    def captura(self,path):
        cap = cv2.VideoCapture(0)
        leido, frame = cap.read()
        if leido == True:
            cv2.imwrite(path, frame)
            print("Foto tomada correctamente")
        else:
            print("Error al acceder a la cámara")

        """
            Finalmente liberamos o soltamos la cámara
        """
        cap.release()