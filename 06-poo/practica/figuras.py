class Figura(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass
    
    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.nombre = __class__.__name__
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f'{self.nombre}: Base: {self.base}, Altura: {self.altura}'
        

class Circulo(object):
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = radio

    def area(self):
        return 3.14159 * (self.radio ** 2)
    
    def perimetro(self):
        return 2 * 3.14159 * self.radio

    def __str__(self):
        return f'{self.nombre}: Radio: {self.radio}'

def probar_figura(figura):
    print(f'Figura: {figura}')
    print(f'Área: {figura.area()}')
    print(f'Perímetro: {figura.perimetro()}')
