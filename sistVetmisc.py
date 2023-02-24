class Medicamento():
    def __init__(self,client):
        mydb = client["sistVete"]
        self.__medicamentos = mydb["medicamentos"]
    
    def verNombreDosis(self):
        for x in self.__medicamentos.find({  "direccion": "C/Mayor, 1" }):
            return print(x)

    def asignarNombreDosis(self,nombre_med,dosis):
        self.__medicamento = self.__medicamentos.insert_one({'Nombre':nombre_med,'Dosis':dosis})  
        return self.__medicamento

class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
        self.__numero_mascotas = len(self.__lista_mascotas)
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 

        # if (self.verNumeroMascotas() < 10 ) and (self.verificarExiste(mascota.verHistoria()) == False): #puedo ingresar
        #         self.__lista_mascotas.append(mascota) 
        #         return True  #ingresada exitosamente
        # else:
        #     return False 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 
    
def main():

    client = pymongo.MongoClient("mongodb+srv://veronicahenaoi:info123@clusterinfo2.8v994es.mongodb.net/?retryWrites=true&w=majority")
    db = client.test

    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue 
            historia=int(input("Ingrese la historia clínica de la mascota: "))
#            verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=int(input("ingrese la cantidad de medicamento de la mascota: "))
                lista_med=[]
                
                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre: ") 
                    dosis = int(input("Ingrese la dosis: ")) 
                    medicamento = Medicamento(client) 
                    medicamento.asignarDosis(dosis)
                    medicamento.asignarNombre(nombre_medicamentos)
                    lista_med.append(medicamento)

            else:
                print("Ya existe una mascota con el numero de historia clínica ingresado.")
            
        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                # fecha = servicio_hospitalario.verFechaIngreso(q) 
                # if fecha != None:    
                print("La fecha de ingreso de la mascota es: " + fecha)
                # else:
                    # print("No se asigno fecha")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            # if servicio_hospitalario.verificarExiste(q) == True:
            #     medicamento = servicio_hospitalario.verMedicamento(q) 
            #     if medicamento != None:    
            #         print("El medicamento suministrado es: " + medicamento)
            #     else:
            #         print("No se asigno medicamento")
            # else:
            #     print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()
    # a={1:sistemaV()}