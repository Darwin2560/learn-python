from persona import Cliente, Empleado

cliente1 = Cliente("Juan", 30)
cliente2 = Cliente("Dael", 22)

print(cliente1)
print(cliente2)

empleado1 = Empleado("Alice", 40, "Gerente", 80000)
empleado2 = Empleado("Bob", 35, "Director", 100000)

empleado1.detalle_persona()
empleado1.detalle_empleado()

print(empleado2)
