class Hospital():
    def __init__(self,nombre,cedula,genero):
        self.nombre = nombre
        self.cedula = cedula
        self.genero = genero
        
class Paciente(Hospital):
    def __init__(self,servicio):
        self.__servicio = servicio
        print('El paciente: ' + self.nombre + ' con cédula: ' + self.cedula + ' es de genero: ' + self.genero + ' se encuentra en el servicio: ' + self.__servicio)

class Enfermero(Hospital):
    def __ini__(self,turnos,rango):
        self.__turnos = turnos #7-19, 19-7
        self.__rango =  rango #auxiliar,jefe,jefe del servicio
        print('El enfermero a cargo del paciente es: '+ self.nombre + ' con cédula: ' + self.cedula + ' es de genero: ' + self.genero + ' y su rango es: ' + self.__rango + ' esta disponible en el turno: ' + self.__turnos)

class Medico(Hospital):
    def __init__(self,turnos,especialidad):
        self.__turnos = turnos #7-19, 19-7
        self.__especialidad = especialidad
        print('El medico a cargo del paciente es: '+ self.nombre + ' con cédula: ' + self.cedula + ' es de genero: ' + self.genero + ' es especoalista en: ' + self.__especialidad + ' y esta disponible en el turno: ' + self.__turnos)
        

h = Hospital('Veronica','11221022','F')
Paciente('general')
Enfermero('Juan','14532222','M','auxiliar','7-19')
Medico('Carlos','14532222','M','internista','7-19')