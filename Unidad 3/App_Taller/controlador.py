# Petición y comunicación entre modelo y vista
from PyQt5 import QtWidgets
import sys
import os 

# Modelo
from modelo import Sistema,client

# Vista
from vista import Ventana, Grafica, Imagen
#from vista_grafica import Grafica


class comunicacion(object):
    def __init__(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__view = Ventana()
        self.__graf = Grafica()
        self.__img = Imagen()
        self.system = Sistema(client)
        self.controller = ctrl(self.__view,self.__graf,self.__img, self.system)
        self.__view.conexionconelcontrolador(self.controller)
        self.__graf.conexionconelcontrolador(self.controller)
        self.__img.conexionconelcontrolador(self.controller)
    
    def main(self):
        self.__view.show()
        sys.exit(self.__app.exec_())

class ctrl(object):
    def __init__(self, view, graf, img, system):
        self.__view = view
        self.__graf = graf
        self.__img = img
        self.system = system

    def agregarpacientes(self,cc,nombre,edad):
        self.system.cedula(cc)
        self.system.nombre(cc,nombre)
        self.system.edad(cc,edad)
        
    def buscarensistema(self,cc):
        nombre,edad=self.system.verificar_db(cc)
        if nombre != None:
            self.__view.rellenar_datos(nombre,edad)
        else:
            print("El paciente no existe")
    
    def buscararchivo(self,path):
        senal = self.system.grafica(path)
        return senal
    
    def guardarimagen(self):
        path = os.getcwd()
        os.startfile(path)
        frame = self.system.captura(path)
        self.__img.ver_imagen(frame)
    
    #def prom_histograma(self,path):
    #    senal = self.system.grafica(path)
    #    promedio = self.system.prom(senal)
    #    self.__graf.Histograma(promedio)
  
    def cambiarvistaagrafico(self):
        self.__graf.show()
        self.__view.close()
    
    def cambiarvistaamenu(self):
        self.__view.show()
        self.__graf.close()
    
    def cambiarvistaaopen(self):
        self.__img.show()
        self.__graf.close()

if __name__ == "__main__":
    controller = comunicacion()
    controller.main()
