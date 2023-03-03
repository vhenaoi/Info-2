import pymongo

class Medicamento():
    def __init__(self,client):
        mydb = client["sistVete"]
        self.__medicamentos = mydb["medicamentos"]
    
    def verNombre(self):
        Nombre=list(self.__medicamentos.find())
        return Nombre[-1]['Nombre']
    
    def verDosis(self):
        Dosis=list(self.__medicamentos.find())
        print('La dosis suministrada es: ' + str(Dosis[-1]['Dosis']))

    def asignarNombre(self,nombre_med):
        x=self.__medicamentos.insert_one({'Nombre':nombre_med})  
    
    def asignarDosis(self,nombre_med,dosis):
        myquery = {"Nombre": nombre_med}
        newvalues = { "$set": { "Dosis":dosis} }
        self.__medicamentos.update_one(myquery, newvalues)
        #self.__medicamento = self.__medicamentos.insert_one({'Dosis':dosis})  
 
        
def main():

    client = pymongo.MongoClient("mongodb+srv://veronicahenaoi:info123@clusterinfo2.8v994es.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    nm=int(input("Ingrese la cantidad de medicamento de la mascota: "))
    m=0
    while m<nm:
        nombre_medicamentos = input("Ingrese el nombre: ") 
        dosis = int(input("Ingrese la dosis: ")) 
        medicamento = Medicamento(client) 
        #medicamento.asignarNombreDosis(nombre_medicamentos,dosis)
        medicamento.asignarNombre(nombre_medicamentos)
        ultimo_nombre=medicamento.verNombre()
        print(f'El nombre del medicamento es {ultimo_nombre}')
        medicamento.asignarDosis(ultimo_nombre,dosis)
        medicamento.verDosis()
        m+=1


if __name__=='__main__':
    main()
