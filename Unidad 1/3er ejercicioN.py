import pymongo

class Medicamento:

    def __init__( self, client ):
        my_data_base = client[ "Tarea" ]
        self.__medicamentos = my_data_base[ "Medicamentos" ]
    
    def MedicamentoVerNombre( self, nombre ):
        listaMedi = list( self.__medicamentos.find( {"Nombre medicamento": nombre} ) )
        return listaMedi[-1]["Nombre"]

    def MedicamentoVerDosis( self, nombre ):
        listaDos = list( self.__medicamentos.find( {"Nombre medicamento": nombre} ) )
        return listaDos[-1]["Dosis"]

    def MedicamentoAsignarNombre( self, nombre_med ):
        medicamento = { "Nombre medicamento": nombre_med }
        self.__medicamentos.insert_one( medicamento )

    def MedicamentoAsignarDosis( self, nombre_med, dosis_med ):
        my_medicamento = { "Nombre medicamento": nombre_med }
        my_dosis = { "$set" : { "Dosis": dosis_med } }
        self.__medicamentos.update_one( my_medicamento, my_dosis )
    


class Mascota:

    def __init__( self, client, historia ):
        my_data_base = client[ "Tarea" ]
        self.__mascota = my_data_base[ "Mascota" ]
        self.__historia = historia

    # Metodos para mostrar
    def MascotaVerNombre( self ):
        lista = list( self.__mascota.find( { "Historia": self.__historia } ) )
        return lista[-1]['Nombre']

    def MascotaVerHistoria( self ):
        lista = list( self.__mascota.find( { "Historia": self.__historia } ) )
        return lista[-1]["Historia"]

    def MascotaVerTipo( self ):
        lista = list( self.__mascota.find( { "Historia": self.__historia } ) )
        return lista[-1]["Gato o perro"]

    def MascotaVerFechaIngreso( self ):
        lista = list( self.__mascota.find( { "Historia": self.__historia } ) )
        return lista[-1]["Fecha"]

    def MascotaVerPeso( self ):
        lista = list( self.__mascota.find( { "Historia": self.__historia } ) )
        return lista[-1]["Peso"]

    def MascotaVerMedicamento( self ):
        lista = list( self.__mascota.find( { "Historia": self.__historia } ) )
        return lista[-1]["Medicamento"]


    # Metodos para asignar
    def MascotaAsignarNombre( self, nombre ):
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Nombre": nombre } }
        self.__mascota.update_one( histo, lista )

    def MascotaAsignarHistoria( self ):
        histo = { "Historia": self.__historia }        
        self.__mascota.insert_one( histo )

    def MascotaAsignarTipo( self, tipo ):    
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Gato o Perro": tipo } }
        self.__mascota.update_one( histo, lista )

    def MascotaAsignarFechaIngreso( self, fecha ):
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Fecha": fecha } }
        self.__mascota.update_one( histo, lista )

    def MascotaAsignarPeso( self, peso ):
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Peso": peso } }
        self.__mascota.update_one( histo, lista )

    def MascotaAsignarMedicamento( self, medicamento ):
        histo = { "Historia": self.__historia }
        lista = { "$set": { "Medicamento": medicamento } }
        self.__mascota.update_one( histo, lista )

    ################### METODO EN MASCOTA PARA PODER AGREGAR OBJETO #####################


    # def MascotaResumir( self, mascota ):    
    #      name = mascota.MascotaVerNombre()
    #      type = mascota.MascotaVerTipo()
    #      weight = mascota.MascotaVerPeso()
    #      date = mascota.MascotaVerFechaIngreso()
    #      med_num = mascota.MascotaVerHistoria()
    #      medicine = mascota.MascotaVerMedicamento()
    #      return { "Nombre": name, "Historia": med_num, "Gato o perro": type, "Fecha": date, "Peso": weight, "Medicamento": medicine }


##########################################################################################

class Sistema:

    def __init__( self, client ):
        my_data_base = client[ "Tarea" ]
        self.__sistema = my_data_base[ "Sistema" ]

    def SistemaEliminarMascota( self, numHisCli ):
        lista = list( self.__sistema.find( { "Historia": numHisCli } ) )
        self.__sistema.delete_one( lista[-1] )

    def SistemaVerMedicamento( self, numHisCli ): # que se esta aministrando a una mascota
        lista = list( self.__sistema.find( { "Historia": numHisCli } ) )
        return lista[-1][ "Medicamento" ]

    def SistemaIngresarMascota( self, mascota ):
        nueva = mascota.__dict__
        x = self.__sistema.insert_one( nueva )
            
    def SistemaVerFechaIngreso( self, numHisCli ):
        lista = list( self.__sistema.find( { "Historia": numHisCli } ) )
        return lista[-1][ "Fecha" ]

    def SistemaVerNumeroDeMascotas( self ):
        lista = list( self.__sistema.find() )
        return len( lista )

    def salir( self ):
        pass

    # ALGUNOS METODOS ADICIONALES PARA QUE EL CODIGO SEA MAS FUNCIONAL

    def SistemaVerificarMascota( self, numHisCli ):
        lista = list( self.__sistema.find( { "Historia": numHisCli } ) )
        if len( lista ) == 0:
            return False
        else: 
            return True 

######################## METODO VALIDAR INT ################################

def validarInt( a ):
    try:
        a = int( a )
        return a
    except:
        b = input( "Ingrese un numero entero: " )
        validarInt( b )

############################################################################

def main():

    client = pymongo.MongoClient( "mongodb+srv://josuepaniagua:Ba5319466@cluster0.megrtoc.mongodb.net/?retryWrites=true&w=majority" )
    db = client.test

    sistema = Sistema( client )

    while True:

        opcion = input( """
        (0) Salir
        (1) Ingresar mascota
        (2) Eliminar mascota
        (3) Fecha de ingreso de la mascota
        (4) Ver lista de medicamentos
        (5) Ver numero de mascotas
        > """ )

        if opcion == 0:
            print( "Fin del programa..." )
            break

        elif opcion == '1': # INGRESAR MASCOTA
            
            if sistema.SistemaVerNumeroDeMascotas() >= 10:
                print( "No hay espacio" )
                continue

            num_historia = validarInt( input("Ingrese el numero de la historia clinica de la mascota: ") )
            if sistema.SistemaVerificarMascota( num_historia ) == True:
                print( "El numero de historia clinica ya esta registrado" )
                continue
                
            name = input( "Ingrese el nombre de la mascota: " )
            type = input( "Ingrese CANINO o FELINO: " )
            weight = input( "Ingrese el peso de la mascota en Kilogramos: " )
            date = input( "Ingrese la fecha dd/mm/aaaa: " )
            med_num = validarInt( input( "Ingrese la cantidad de medicamentos: " ) )
            medicamentos = {}

            for i in range( 0, med_num ):
                medicamento = Medicamento( client )
                nombre_medicamento = input( "Ingrese el nombre del medicamento: " )
                dosis = input( "Ingrese la dosis del medicamento: " )
                medicamento.MedicamentoAsignarNombre( nombre_medicamento )
                medicamento.MedicamentoAsignarDosis( nombre_medicamento, dosis )
                medicamentos[ nombre_medicamento ] = dosis
            
            pet = Mascota( client, num_historia )
            pet.MascotaAsignarHistoria()
            pet.MascotaAsignarNombre( name )
            pet.MascotaAsignarTipo( type )
            pet.MascotaAsignarPeso( weight )
            pet.MascotaAsignarFechaIngreso( date )
            pet.MascotaAsignarMedicamento( medicamentos )

############################# NO FUNCIONA #############################

            sistema.SistemaIngresarMascota( pet )

            print( f"Mascota {name} ingresada..." )

        elif opcion == '2': # ELIMINAR MASCOTA
            
            num_historia = validarInt( input( "Ingrese el numero de la historia clinica que desea eliminar: " ) )
            if sistema.SistemaVerificarMascota == False:
                print( "El numero de la historia clinica ingresado no existe..." )
                continue
            

        elif opcion == '3': # FECHA DE INGRESO DE LA MASCOTA
            
            num_historia = validarInt( input( "Ingrese el numero de la historia clinica que desea eliminar: " ) )
            if sistema.SistemaVerificarMascota == False:
                print( "El numero de la historia clinica ingresado no existe..." )
                continue
            
        elif opcion == '4': # VER LISTA DE MEDICAMENTOS (que se esta administrando a una mascota)
            
            pass
            
        elif opcion == '5': # VER NUMERO DE MASCOTAS
        
            print( sistema.SistemaVerNumeroDeMascotas() )

        else:
            print( "Opcion no valida" )

if __name__ == '__main__':
    main()

    

    