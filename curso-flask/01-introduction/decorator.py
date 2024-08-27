def decorator(func):
    def decorate(*args):
        print('Inicia la ejecución de la funcion: ', func.__name__)
        func(*args)
        print('Finaliza la ejecución de la función: ', func.__name__)
    return decorate

@decorator
def hello(nombre):
    print(f'Hello, {nombre} 👋!')

hello('Juan')
