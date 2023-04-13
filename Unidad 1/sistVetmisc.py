class Medicamento:
    def __init__(self):
        self.__nombre = ""
        self.__dosis = 0
    
    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis
    
    def asignarNombre(self,temp):
        self.__nombre = temp
    def asignarDosis(self,temp):
        self.__dosis = temp
    
class Mascota:
    def __init__(self):
        self.__nombre = ""
        self.__tipo = ""
        self.__num_historia = 0
        self.__peso = 0
        self.__fecha_ingreso = ""
        self.__lista_medicamentos = []
        
    def verNombre(self):
        return self.__nombre    
    def asignarNombre(self,temp):
        self.__nombre = temp  
    
    def asignarTipo(self,temp):
        self.__tipo = temp 
        
    def asignarHistoria(self,temp):
        self.__num_historia = temp 
    def verHistoria(self):
        return self.__num_historia
        
    def asignarPeso(self,temp):
        self.__peso = temp 
        
    def asignarFechaIngreso(self,temp):
        self.__fecha_ingreso = temp 
    def verFechaIngreso(self):
        return self.__fecha_ingreso 

    def asignarMedicamentos(self,m):
        self.__lista_medicamentos = m
    def verMedicamentos(self):
        return self.__lista_medicamentos
    
class Sistema:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarMascota(self,nhc):
        encontrado = False
        for m in self.__lista_mascotas:
            if m.verHistoria() == nhc:
                encontrado = True
                break
        return encontrado
    
    def ingresarMascota(self,m):
        self.__lista_mascotas.append(m)
    
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas)
    
    def verPosicionMascota(self,nhc):
        posicion = 0
        if self.verificarMascota(nhc) == False:
            posicion = -1 #si no esta devuelvo posicion negativa = NO EXISTE
            return posicion
        for m in self.__lista_mascotas:
            if m.verHistoria() == nhc:
                return posicion
            posicion = posicion + 1
    def eliminarMascota(self,nhc):
        #tenemos que saber la posicion de la mascota
        posicion = self.verPosicionMascota(nhc)
        if posicion >= 0: #la mascota si existe
            del self.__lista_mascotas[posicion]
            return True
        else:
            #la mascota no existe, no se puede eliminar
            return False
    def recuperarMascota(self,nhc):
        #puedo mezclar metodos que ya he construido
        #1 buscar la posicion de la mascota
        posicion = self.verPosicionMascota(nhc)
        if posicion < 0:
            #no existe la mascota
            return None
        mascota = self.__lista_mascotas[posicion]
        return mascota
    
    def verFechaIngresoMascota(self,nhc):
        m = self.recuperarMascota(nhc)
        if m == None:
            return "La mascota no está en el sistema"
        return m.verFechaIngreso()

#funciones         
def ingresoNumerico(mensaje):
    valido = False
    while valido == False:
        try:
            valor = int(input(mensaje))
            valido = True
        except ValueError:
            print("ingrese un dato numerico ...")
    return valor

def main():
    #creamos el sistema
    sistema = Sistema()
    while True:
        opcion = ingresoNumerico("Ingrese 0 para salir, 1 para ingresar mascota, 2 para eliminar, 3 ver Fecha Ingreso, 4 ver lista medicamentos, 5 ver numero de mascotas ")
        if opcion == 0:
            print("Fin del programa ...")
            break
        elif opcion == 5:
            print("El sistema tiene " + str(sistema.verNumeroMascotas()) + " mascotas")
        elif opcion == 4:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = int(input("Ingrese Numero de Historia Clinica: "))
            if sistema.verificarMascota(nhc) == False:
                print("La mascota no esta en el sistema ...")
                continue
            #recupero la mascota de la base de datos
            m = sistema.recuperarMascota(nhc)
            lista_medicamentos = m.verMedicamentos()
            print("La mascota: " + m.verNombre() + " tiene los sgtes medicamentos:")
            for medicamento in lista_medicamentos:
                print("Medicamento con nombre: " + medicamento.verNombre() + " dosis " + str(medicamento.verDosis()))
        elif opcion == 3:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = int(input("Ingrese Numero de Historia Clinica: "))
            if sistema.verificarMascota(nhc) == False:
                print("La mascota no esta en el sistema ...")
                continue
            print(sistema.verFechaIngresoMascota(nhc))
        elif opcion == 2:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = int(input("Ingrese Numero de Historia Clinica: "))
            resultado = sistema.eliminarMascota(nhc)
            if resultado == True:
                print("Se elimino exitosamente la mascota del sistema ...")
            else:
                print("No se elimino la mascota del sistema, posiblemente no exista ...")
        elif opcion == 1:
            #1. debo verificar que haya espacio en el servicio
            if sistema.verNumeroMascotas() >= 10:
                print("No hay espacio ...")
                continue
            #2. solicitar numero de historia clinica y ver que no este
            nhc = ingresoNumerico("Ingrese Numero de Historia Clinica: ")
            if sistema.verificarMascota(nhc) == True:
                print("La mascota ya esta en el sistema ...")
                continue
            #3. Si la historia no esta pido los datos restantes
            n = input("Ingrese el nombre de la mascota: ")
            t = input("Ingrese CANINO o FELINO: ")
            p = ingresoNumerico("Ingrese el pesos de la mascota en kilogramos")
            f = input("Ingrese la fecha dd/mm/aaaa : ")
            nm = int(input("Ingrese el numero de medicamentos: "))
            lista_medicamentos = []
            #4. por cada medicamento solicito los datos
            for i in range(0,nm):
                nombre_medicamentos = input("Ingrese el nombre: ")
                dosis = ingresoNumerico("Ingrese la dosis: ")
                medicamento = Medicamento()
                medicamento.asignarDosis(dosis)
                medicamento.asignarNombre(nombre_medicamentos)
                lista_medicamentos.append(medicamento)
            #5. crear la mascota y asignarle la informacion
            mascota = Mascota()
            mascota.asignarHistoria(nhc)
            mascota.asignarNombre(n)
            mascota.asignarTipo(t)
            mascota.asignarPeso(p)
            mascota.asignarFechaIngreso(f)
            mascota.asignarMedicamentos(lista_medicamentos)
            #6. Ingresar la mascota al sistema
            sistema.ingresarMascota(mascota)
            print("Mascota " + n + " ingresada ...")
        else:
            print("Opcion no valida: ")


if __name__ == '__main__':
    main()