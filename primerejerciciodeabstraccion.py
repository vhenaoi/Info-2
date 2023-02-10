class Persona():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

# Setters
    def asignarNombre(self,nombre):
        self.__nombre = nombre
    def asignarCedula(self,cedula):
        self.__cedula = cedula
    def asignarGenero(self,genero):
        self.__genero = genero

# getters 
    def verNombre(self): 
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero

    def borrarNombre(self):
        del self.__nombre
    def borrarCedula(self):
        del self.__cedula
    def borrarGenero(self):
        del self.__genero

    def caminar(self):        
        print(input("ingrese direccion: "))

    def comer(self):
        print("El paciente debe comer cada 8 horas")

    def imprimirInfo(self):
        print (self.__nombre,self.__cedula,self.__genero)

class Paciente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__servicio = ""

    def asignarServicio(self, servicio):
        self.__servicio = servicio
    def verServicio(self):
        return self.__servicio

class Empleado_Hospital(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__turno = {"Mañana":"7-19","Noche":"19-7","Corrido":"Corrido"}

    def asignarTurno(self, turno):
        self.__turno = turno

    def verturno(self):
        return self.__turno

class Enfermera(Empleado_Hospital):
    def __init__(self):
        Empleado_Hospital.__init__(self) # Invocando el constructor de la clase padre de la cual esta heredando 
        # super().__init__() # Este metodo hace exactamente lo mismo que le anterior, invocar el constructor de la clase padre 
        self.__rango = ''

    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self, rango):
        return self.__rango

class Medico(Empleado_Hospital):
    def __init__(self):
        Empleado_Hospital.__init__(self)
        
        self.__especialidad = ''
    
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = ''
    def verEspecialidad(self, especialidad):
        return self.__especialidad

# k = 9 # objeto de la clase int
p1 = Paciente()
p2 = Paciente()
e1 = Enfermera()
e1.asignarNombre("Pepito")
e1.asignarCedula("1345132")
e1.asignarGenero("F")
print(e1.verturno()["Mañana"])
e1.imprimirInfo()
listaPaciente={}

listaPaciente[123] = p1
listaPaciente[234] = p2
# print(listaPaciente)

# pacientes.asignarNombre('Juan José Trejo')
# pacientes.asignarCedula(1085341857)
# pacientes.asignarGenero('Masculino')
# print(pacientes.verNombre())
# print(pacientes.verCedula())
# print(pacientes.verGenero())