
import pymongo
import scipy.io as sio
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import cv2

class Sistema():
    def __init__(self,client):
        mydb = client["Hospital"]
        self.__neurologia = mydb["neurologia"]
    
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
    
    def signal(self,cedula,path_signal):
        myquery = {'Cédula':cedula}
        newvalues = { "$set": { "Señal":path_signal} }
        self.__neurologia.update_one(myquery, newvalues) 
    
    def signal_img(self,cedula,path_img1):
        myquery = {'Cédula':cedula}
        newvalues = { "$set": { "Imagen Señal":path_img1} }
        self.__neurologia.update_one(myquery, newvalues) 
    
    def hm_color(self,cedula,path_hm):
        myquery = {'Cédula':cedula}
        newvalues = { "$set": { "Mapa de calor":path_hm} }
        self.__neurologia.update_one(myquery, newvalues) 

    def hm_BN(self,cedula,path_bn):
        myquery = {'Cédula':cedula}
        newvalues = { "$set": { "Mapa de calor BN":path_bn} }
        self.__neurologia.update_one(myquery, newvalues) 
        

        
def main():
    
    #client = pymongo.MongoClient("mongodb+srv://veronicahenaoi:info123@clusterinfo2.8v994es.mongodb.net/?retryWrites=true&w=majority")
    #db = client.test

    #creamos el sistema
    #sistema = Sistema(client)
    
    #Ejemplo:
    while True:
        ## Etapa 1
        while True:
            try:
                cc = int(input("Ingrese su número de cédula: "))
                break            
            except:
                print('La cédula debe ser un número')
        while True:
            try:
                n = input("Ingrese su nombre: ")     
                if n.isalpha():
                    break
                else:
                    print('El nombre deben ser letras')
            except:
                print('El nombre deben ser letras')
        while True:
            try:
                e = int(input("Ingrese su edad: "))   
                break          
            except:
                print('La edad debe ser un número')
        #sistema.cedula(cc)
        #sistema.nombre(cc,n)
        #sistema.edad(cc,e)
        print("SISTEMA DE LECTURA DE SEÑALES")
        path_signal = input("Introduzca la ruta de la señal: ")
        #sistema.signal(cc,path_signal)
        mat_contents = sio.loadmat(path_signal) 
        senal = mat_contents['data'] 
        sensores = senal.shape[0] 
        puntos = senal.shape[1] 
        epocas = senal.shape[2] 
        senal_continua = np.reshape(senal,(sensores,puntos*epocas),order = 'F') 
        while True:
            print("MENÚ 1\n1. Ver tamaño de la señal\n2. Graficar una señal de EEG continua\n3. Graficar una epoca de señal de EEG\n4. Graficar la señal de un color determinado\n5. Análisis de los datos\n6. Salir.")
            opcion = int(input("Seleccione una opción de menú 1: "))
            if opcion == 1:
                print("TAMAÑO DE LA SEÑAL")
                print("La señal tiene dimensión: "+str(senal.ndim) + " y una forma de: " + str(senal.shape)) 
            elif opcion == 2:
                print("SEÑAL CONTINUA")
                plt.plot(senal_continua[0,:]) 
                plt.show() 
            elif opcion == 3:
                print("SEÑAL POR ÉPOCAS")
                plt.plot(senal[0,:,0]) 
                plt.show() 
            elif opcion == 4:
                print("SEÑAL PERSONALIZADA")
                c = input("Ingrese el color que desea aplicar a la señal en formato hexadecimal: ") 
                plt.plot(senal_continua[0,0:1999],color=c) 
                path_signal_img = r"E:\Academico\Universidad\Cursos\Repositorios\Info-2\OpenCV\signal.png"
                #sistema.signal_img(cc,path_signal_img)
                plt.savefig(path_signal_img)
                plt.show() 
            elif opcion == 5:
                while True:
                    print("SISTEMA DE ANÁLISIS DE SEÑALES")
                    print("MENÚ 2\n1. Ver el promedio de las 8 filas de la señal continua\n2. Ver el histograma del promedio del punto 1\n3. Ver una imagen de calor \n4. Imagen en blanco y negro\n5. Salir.")
                    opcion2 = int(input("Seleccione una opción del menú 2: "))
                    if opcion2 == 1:
                        print("PROMEDIO")
                        pd_senal=pd.DataFrame(senal_continua)
                        promedio=pd_senal.apply(lambda x : x.mean(), axis=1, args=())
                        print(promedio)
                    elif opcion2 == 2:
                        print("HISTOGRAMA")
                        sns.kdeplot(promedio)
                        plt.show()
                    elif opcion2 == 3: 
                        print("MAPA DE CALOR")
                        df = pd.DataFrame(senal[0,:100,:-100])
                        hm = sns.heatmap(df, cmap="YlGnBu")
                        path_hm = r"E:\Academico\Universidad\Cursos\Repositorios\Info-2\OpenCV\hmcolor.png"
                        #sistema.hm_color(cc,path_hm)
                        plt.savefig(path_hm)
                        plt.show()
                    elif opcion2 == 4:
                        print("MAPA DE CALOR EN BLANCO Y NEGRO")
                        img=cv2.imread(path_hm)
                        imgR=img[:,:,0]
                        path_BN = r"E:\Academico\Universidad\Cursos\Repositorios\Info-2\OpenCV\hmBN.png"
                        cv2.imwrite(path_BN,imgR)
                        #sistema.hm_BN(cc,path_BN)
                        cv2.namedWindow('Heatmap',0)
                        cv2.imshow('Heatmap',imgR)
                    elif opcion2 == 5:
                        break
                    else:
                        print("Seleccione una opcion correcta")
            elif opcion == 6:
                break
        print("Finalizo el programa")
        continuar = int(input("Si desea analizar otro sujeto presione 1, si desea salir presione cualquier otro número: "))
        if continuar == 1:
            pass
        else:
            break


if __name__ == '__main__':
    main()