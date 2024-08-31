class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def detalle_persona(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


class Cliente(Persona):
    pass


class Empleado(Persona):
    def __init__(self, nombre, edad, puesto, salario):
        # super().__init__(nombre, edad)
        Persona.__init__(
            self, nombre, edad
        )  # Alternativa para herencia anidada (en lugar de super().__init__())
        self.puesto = puesto
        self.salario = salario

    def detalle_empleado(self):
        # super().detalle_persona()
        Persona.detalle_persona(
            self
        )  # Alternativa para herencia anidada (en lugar de super().detalle_persona())  # Sin usar super()
        print(f"Puesto: {self.puesto}, Salario: {self.salario:,.2f}")

    def __str__(self):
        # return super().__str__() + f', Puesto: {self.puesto}, Salario: {self.salario:,.2f}'
        return (
            Persona.__str__(self)
            + f", Puesto: {self.puesto}, Salario: {self.salario:,.2f}"
        )
        pass
