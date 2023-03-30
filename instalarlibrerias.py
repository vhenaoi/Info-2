import os
from os import system

nombre_env = input('Ingrese el nombre del entorno: ')
def create():
    system("python -m pip install --upgrade pip")
    system("python -m pip --version")
    system("python -m pip install --user virtualenv")
    current = os.getcwd()
    system("python -m venv "+ current+'/'+str(nombre_env))
    system(current+'/'+str(nombre_env)+"/"+"Scripts/activate")
    system("python -V")
    # En el letrero que aparece en la parte inferior derecha presione la opción "Si" 
    # Si no alcanzo a presionar la opción de click en la version de python que aparece
    # Al lado de "Python" y en el menú que se muestra busque la opcion recomendada o la opción 
    # Que tenga el nombre que usted le dio a su entorno. 
    #system("python -m pip install -r "+ current+'/'+ "requirements.txt") #Manera optima de ejecutar las lineas (18-25)
    system("python -m pip install numpy")
    system("python -m pip install matplotlib")
    system("python -m pip install pandas")
    system("python -m pip install scipy")
    system("python -m pip install opencv-python")
    system("python -m pip install mne")
    system("python -m pip install Seaborn")
    system("python -m pip install pingouin")
    print("Su entorno esta listo para ser utilizado")

    
create()


