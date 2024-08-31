class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def moverse(self):
        print(f"{self.nombre} se mueve")


class Atleta(Persona):
    def moverse(self):
        print(f"{self.nombre} corre")


class Ciclista(Persona):
    def moverse(self):
        print(f"{self.nombre} se mueve en bicicleta")
