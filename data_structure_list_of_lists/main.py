# Hay diferentes formas de representar los datos, y cada forma
# tiene su propia forma de recorrerlos para procesarlos

# Resuelva las siguientes casos, donde la variable 'notas' contiene 
# las notas de los 3 parciales para 3 materias de un mismo estudiante

# Recuerde:
# - Analice primero, planee/diseñe una solución, luego escriba el código
# - Utilice comentarios para explicar las partes importantes
# - No utilice números mágicos, si es el caso utilice constantes
# - Realice sus propias pruebas para verificar que todo funciona


########################################################################
# Caso 1: Lista de Listas

notas = [
  ["Calculo", 3.5, 2.5, 1.5],
  ["Quimica", 2.5, 3.0, 5.0],
  ["Deporte", 2.4, 2.0, 2.2],
  ["Logica", 1.5, 4.0, 4.5]
]

# 1.1 Calcula la nota final de cada materia (30%, 30% y 40%), 
# y agregue el valor a los datos
def c11_final():
    global notas 
    for i in range(len(notas)):
        nota1 = notas[i][1]*0.3
        nota2 = notas[i][2]*0.3
        nota3 = notas[i][3]*0.4
        nota_final = nota1+nota2+nota3 
        notas[i].append(nota_final)
  
  
# 1.2 Calcule el promedio de las notas del Estudiante
def c12_promedio():
    global notas 
    suma_notas = 0
    for i in range(len(notas)):
        suma_notas+=notas[i][4]
    print("El promedio de las notas del estudiante es de : ",suma_notas/len(notas))
    

# Llamar funciones, y mostrar Resultados
print("\n------------------------ Punto 1 ------------------------\n")
c11_final()
c12_promedio()
########################################################################
# Caso 2: Diccionario de Listas

notas = {
  "Calculo": [3.5, 2.5, 1.5],
  "Quimica": [2.5, 3.0, 5.0],
  "Deporte": [2.4, 2.0, 2.2],
  "Logica": [1.5, 4.0, 4.5]
}

# 2.1 Calcula la nota final de cada materia (30%, 30% y 40%), 
# y agregue el valor a los datos
def c21_final():
    global notas
    for key, value in notas.items():
        nota1 = value[0]*0.3
        nota2 = value[1]*0.3
        nota3 = value[2]*0.4
        nota_final = nota1+nota2+nota3
        notas[key].append(nota_final)

# 2.2 Calcule el promedio de las notas del Estudiante
def c22_promedio():
    global notas
    suma_notas = 0
    for key, value in notas.items():
        suma_notas += value[3]
    print(f"El promedio de las notas del estudiante es de: {suma_notas/len(notas)}")
# Llamar funciones, y mostrar Resultados
print("\n------------------------ Punto 2 ------------------------\n")
c21_final()
c22_promedio()
########################################################################
# Caso 3: Diccionario de Diccionarios

notas = {
  "Calculo": {"pp": 3.5, 
              "sp": 2.5, 
              "tp": 1.5},
  "Quimica": {"pp": 2.5, 
              "sp": 3.0, 
              "tp": 5.0},
  "Deporte": {"pp": 2.4, 
              "sp": 2.0,
              "tp": 2.2},
  "Logica":  {"pp": 1.5, 
              "sp": 4.0, 
              "tp": 4.5}
}

# 3.1 Calcula la nota final de cada materia (30%, 30% y 40%), 
# y agregue el valor a los datos
def c31_final():
    global notas
    for key, value in notas.items():
        nota1 = value["pp"]*0.3
        nota2 = value["sp"]*0.3
        nota3 = value["tp"]*0.4
        nota_final = nota1+nota2+nota3
        notas[key]["nf"] = nota_final
  

# 3.2 Calcule el promedio de las notas del Estudiante
def c32_promedio():
    global notas
    suma_notas = 0
    for key, value in notas.items():
        suma_notas += value["nf"]
    print(f"El promedio de las notas del estudiante es de: {suma_notas / len(notas)}")


# Llamar funciones, y mostrar Resultados
print("\n------------------------ Punto 3 ------------------------\n")
c31_final()
c32_promedio()
# Caso 4: Lista de Diccionarios

notas = [
  { "nombre": "Calculo", 
    "pp": 3.5, 
    "sp": 2.5, 
    "tp": 1.5},
  { "nombre": "Quimica",
    "pp": 2.5, 
    "sp": 3.0, 
    "tp": 5.0},
  { "nombre": "Deporte",
    "pp": 2.4, 
    "sp": 2.0,
    "tp": 2.2},
  { "nombre": "Logica",
    "pp": 1.5, 
    "sp": 4.0, 
    "tp": 4.5}
]

# 4.1 Calcula la nota final de cada materia (30%, 30% y 40%), 
# y agregue el valor a los datos
def c41_final():
  global notas
  for i in range(len(notas)):
      nota1 = notas[i]["pp"]*0.3
      nota2 = notas[i]["sp"]*0.3
      nota3 = notas[i]["tp"]*0.4
      nota_final = nota1+nota2+nota3
      notas[i]["nf"] = nota_final

# 4.2 Calcule el promedio de las notas del Estudiante
def c42_promedio():
  global notas
  suma_notas = 0
  for i in range(len(notas)):
    suma_notas += notas[i]["nf"]
  print(f"El promedio de las notas del estudiante es de: {suma_notas / len(notas)}")


# Llamar funciones, y mostrar Resultados
print("\n------------------------ Punto 4 ------------------------\n")
c41_final()
c42_promedio()