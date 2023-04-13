class ave:

    def __init__(self,tipo,vuela,comida):
        self.ave =  tipo
        self.vuelo = vuela
        self._oviparos = True
        self.pico = True

    def comer(self,comida):
        print("Este tipo de ave come normalmente : ", comida)

    def volar(self):
        print("Este tipo de ave puede volar : ", self.vuelo)

class ganso(ave):

    def __init__(self,tipo,vuela,accion,pata):
        ave.__init__(self,tipo,vuela)
        self.habilidad = accion
        self.patas = pata

    def destreza(self):
        print("Esta ave puede : ", self.habilidad)

class pato(ganso):
    pass
class gallina(ave):
    pass

p=ave("gallina","Si")
p.volar()
p.comer("Maiz")

g=ganso("carnivoro",True,"nadar","4")
g.destreza()
