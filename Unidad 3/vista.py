# Respuesta grafica
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
#importamos las librerías necesarias
from PyQt5 import QtWidgets, uic
import pyqtgraph as pg
import cv2

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("menu_ingreso.ui",self) #Lee el archivo de QtDesigner


        #Conectar botones a funciones
        self.verificar.clicked.connect(self.verificar_dato)
        self.agregar.clicked.connect(self.agregar_dato)
        self.salir.clicked.connect(self.cerrar)
        self.continuar.setEnabled(False)
        self.continuar.clicked.connect(self.continuar_dato) 


    def conexionconelcontrolador(self,control):
        self.mi_controlador = control

    def verificar_dato(self):
        self.mi_controlador.buscarensistema(self.input_cedula.text())
        
    def rellenar_datos(self,nombre,edad):
        self.verificar.setEnabled(False)
        self.input_nombre.setText(nombre)
        self.input_edad.setText(str(edad))
        self.continuar.setEnabled(True)
        

    def agregar_dato(self):
        self.mi_controlador.agregarpacientes(self.input_cedula.text(),self.input_nombre.text(),self.input_edad.text())
        self.agregar.setEnabled(False)
        self.continuar.setEnabled(True)
 
    def cerrar(self):
        self.close()
    
    def continuar_dato(self):
        self.mi_controlador.cambiarvistaagrafico()

#Carga la interfaz gráfica y conecta los botones
class Grafica(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("graficos.ui",self) #Lee el archivo de QtDesigner

        # Instanciar figura
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        #Conectar botones a funciones
        self.boton_graficar.clicked.connect(self.funcion_graficar)
        self.atras.clicked.connect(self.menu)
        self.salir.clicked.connect(self.cerrar)
 
    def conexionconelcontrolador(self,control):
        self.mi_controlador = control
   
    def funcion_graficar(self):
        senal=self.mi_controlador.buscararchivo(self.ruta_senal.text()[1:-1])
        #promedio = self.mi_controlador.prom_histograma(self.ruta_senal.text()[1:-1])
        if self.tipo_grafica.currentText() == "EEG continuo":
            self.EEG(senal)
        elif self.tipo_grafica.currentText() == "EEG una epoca":
            self.epoca(senal) 
        else:
            print('Seleccione una grafica')

    def EEG(self,senal):
        scene = QtWidgets.QGraphicsScene()
        self.cuadro_grafico.setScene(scene)
        self.plt = pg.PlotWidget()
        plot_item = self.plt.plot(senal[0,:])
        proxy_widget = scene.addWidget(self.plt)

    def epoca(self,senal):
        scene = QtWidgets.QGraphicsScene()
        self.cuadro_grafico.setScene(scene)
        self.plt = pg.PlotWidget()
        plot_item = self.plt.plot(senal[0,:2000])
        proxy_widget = scene.addWidget(self.plt)

    def menu(self):
        self.mi_controlador.cambiarvistaamenu()
 
    def cerrar(self):
        self.mi_controlador.cambiarvistaaopen()

#Carga la interfaz gráfica y conecta los botones
class Imagen(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("Grafico_opencv.ui",self) #Lee el archivo de QtDesigner

        #Conectar botones a funciones
        self.boton_graficar.clicked.connect(self.ver_imagen)
        self.atras.clicked.connect(self.menu)
        self.guardar.clicked.connect(self.guardar_imagen)
 
    def conexionconelcontrolador(self,control):
        self.mi_controlador = control
   
    def ver_imagen(self,frame):
        if self.tipo_grafica.currentText() == "Canal B":
            frame=frame[:,:,0]
        elif self.tipo_grafica.currentText() == "Canal G":
            frame=frame[:,:,1]
        elif self.tipo_grafica.currentText() == "Canal R":
            frame=frame[:,:,2]
        else:
            print('Seleccione una grafica')
        cv2.imshow('ventana',frame)

    def guardar_imagen(self):
        self.mi_controlador.guardarimagen()
        print('guardar')

    def menu(self):
        self.mi_controlador.cambiarvistaamenu()
 

## se crea la instancia de la aplicación
#app = QtWidgets.QApplication(sys.argv)
## se crea la instancia de la ventana
#miVentana = Ventana()
## se muestra la ventana 
#miVentana.show()
## se entrega el control al sistema operativo
#sys.exit(app.exec_())