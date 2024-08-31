from figuras import Circulo, Rectangulo, probar_figura


def main():
    while True:
        menu = """
            AREAS Y PERIMETROS DE FIGURAS GEOMETRICAS

            1. Rectangulo
            2. Circulo
            3. Salir
            Ingrese una opcion: """

        opcion = input(menu)

        if opcion == "1":
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            rectangulo = Rectangulo(base, altura)
            probar_figura(rectangulo)
        elif opcion == "2":
            radio = float(input("Ingrese el radio del circulo: "))
            circulo = Circulo(radio)
            probar_figura(circulo)
        elif opcion == "3":
            print("Gracias por utilizar el programa.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
