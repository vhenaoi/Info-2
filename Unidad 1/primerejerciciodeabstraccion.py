class Persona():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

# Setters
    def asignarNombre(self,rol):
        self.__nombre = input('Ingrese el nombre del ' + rol +': ')
    def asignarCedula(self,rol):
        while True:
            self.__cedula = input('Ingrese la cédula del ' + rol +': ')
            try: 
                assert int(self.__cedula)
                return int(self.__cedula)
            except:
                print('Debe ingresar un número, sin comas ni puntos')
                pass

    def asignarGenero(self,rol):
        self.__genero = input('Ingrese el genero del ' + rol +': ')

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

    def imprimirInfo(self):
        print (self.__nombre,self.__cedula,self.__genero)

    def guardarInfo(self):
        return self.__nombre,self.__cedula,self.__genero
    
class Sistema(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__lista_pacientes = []
        self.__lista_nombre = []
        self.__lista_cedula = []
        self.__lista_genero = []
        self.__diccionario_pacientes = {'Nombre':[],'Cédula':[],'Genero':[]}
        
    def numPacientes(self):
        self.__numero_pacientes = len(self.__lista_pacientes)
        return self.__numero_pacientes

    def ingresar(self,rol):
        p = Paciente()
        p.asignarNombre(rol)
        p.asignarCedula(rol)
        p.asignarGenero(rol)
        p.asignarServicio()
        self.__lista_pacientes.append(p.guardarInfo())
        self.__lista_nombre.append(p.verNombre())
        self.__lista_cedula.append(p.verCedula())
        self.__lista_genero.append(p.verGenero())
        self.__diccionario_pacientes.update({'Nombre':self.__lista_nombre,'Cédula':self.__lista_cedula,'Genero':self.__lista_genero})
        #print(self.__lista_pacientes)
        #print(self.__diccionario_pacientes)
        #print(self.numPacientes())
        print('Se ingreso el paciente: \n' + str(p.guardarInfo()))

    def verDatosPacientesLista(self):
        cedula = str(input('Ingresar la cédula del Paciente que busca en la lista: '))
        for c in self.__lista_pacientes:
            if cedula == c[1]:
                return print(c)
            
    def verDatosPacientesDiccionario(self):
        cedula = str(input('Ingresar la cédula del Paciente que busca en el diccionario: '))
        for p,c in enumerate(self.__diccionario_pacientes['Cédula']):
            if cedula == str(c):
                return print('Nombre : ' +self.__diccionario_pacientes['Nombre'][p], 'Cédula : ' +self.__diccionario_pacientes['Cédula'][p], 'Genero : ' +self.__diccionario_pacientes['Genero'][p] )

class Paciente(Persona):
    def __init__(self):
        super().__init__()
        self.__servicio = ""

    def asignarServicio(self):
        self.__servicio = input('Ingresar el servicio: ')
    def verServicio(self):
        return self.__servicio

class Empleado_Hospital(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__turno = {"Mañana":"7-19","Noche":"19-7","Corrido":"Corrido"}

    def asignarTurno(self, turno):
        self.__turno = turno

    def verTurno(self):
        return self.__turno

class Enfermera(Empleado_Hospital):
    def __init__(self):
        Empleado_Hospital.__init__(self) # Invocando el constructor de la clase padre de la cual esta heredando 
        # super().__init__() # Este metodo hace exactamente lo mismo que le anterior, invocar el constructor de la clase padre 
        self.__rango = ''

    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self):
        return self.__rango

class Medico(Empleado_Hospital):
    def __init__(self):
        Empleado_Hospital.__init__(self)
        
        self.__especialidad = ''
    
    def asignarEspecialidad(self, especialidad):
        self.__especialidad = especialidad
    def verEspecialidad(self):
        return self.__especialidad

#p1 = Paciente()
#p2 = Paciente()
#e1 = Enfermera()
#e1.asignarNombre("Pepito")
#e1.asignarCedula("1345132")
#e1.asignarGenero("F")
#print(e1.verturno()["Mañana"])
#e1.imprimirInfo()
#listaPaciente={}
#
#listaPaciente[123] = p1
#listaPaciente[234] = p2
#print(listaPaciente)

# pacientes.asignarNombre('Juan José Trejo')
# pacientes.asignarCedula(1085341857)
# pacientes.asignarGenero('Masculino')
# print(pacientes.verNombre())
# print(pacientes.verCedula())
# print(pacientes.verGenero())

def main():
    s = Sistema()

    while True:
        opcion = int(input('1. Ingresar paciente - 2. Ver datos del paciente - 3. Ver el número de pacientes en el sistema - 4. Salir\n Ingrese el número de la opción requerida: '))
        if opcion == 1:
            s.ingresar('Paciente')
        elif opcion == 2:
            s.verDatosPacientesDiccionario()
        elif opcion == 3:
            print(s.numPacientes())
        elif opcion == 4:
            break

if __name__ == '__main__':
    main()

                     