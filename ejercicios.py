"""
1# Escribir un programa que pida al usuario su nombre y lo salude.
"""
def saludaNombre(nombre: str) -> str:
  saludo = print(f"Hola",nombre,"!")
  return saludo

def solicitaNombre():
  nombre = input("Favor ingresa tu nombre: ")
  nombre = nombre.capitalize()
  saludaNombre(nombre)

print("\n" + "*" * 20 + " Ejercicio 01 " + "*" * 20)
solicitaNombre()

"""
2# Escribir un programa que calcule la suma de los números pares del 1 al 100.
"""
def sumaPares() -> int:
  listado = list(range(1,101, 1))
  filterValues = filter(lambda x: not x % 2, listado)
  suma = sum(filterValues)
  return suma

print("\n" + "*" * 20 + " Ejercicio 02 " + "*" * 20)
print("La sumatoria de números pares del 1 al 100 es:", sumaPares())

"""
3# Escribir un programa que pida al usuario un número entero positivo y calcule su factorial.
"""
def calculaFactorial(numero: int) -> str:
  factorial = 1
  for val in range(1, numero + 1):
    factorial = factorial * val
  result = print(f"El factorial de", numero, "es:", factorial)
  return result

def solicitaNumero():
  numero = input("Favor ingresa un número entero positivo para calcular su factorial: ")
  numero = int(numero)
  calculaFactorial(numero)

print("\n" + "*" * 20 + " Ejercicio 03 " + "*" * 20)
solicitaNumero()

"""
4# Escribir un programa que pida al usuario un número entero positivo y verifique si es primo.
"""
def verificaPrimo() -> str:
  numero = input("Favor ingresa un número entero positivo, para verificar si es primo: ")
  numero = int(numero)
  raiz = int(numero ** (1/2))

  if (raiz*raiz == numero):
    print("El número", numero, "no es primo, es un cuadrado perfecto!")

  for n in range(2, numero):
    if numero % n == 0:
      print("No es primo,", n, "es un divisor de", numero)
      return False
  print("El número", numero, "es primo")
  return True

print("\n" + "*" * 20 + " Ejercicio 04 " + "*" * 20)
verificaPrimo()

"""
5# Escribir un programa que reciba una lista de números enteros 
y devuelva la suma de los elementos de la lista.
"""
listado = list(range(1,1000, 1))

def sumaLista(listado: list) -> int:
  suma = sum(listado)
  return suma

print("\n" + "*" * 20 + " Ejercicio 05 " + "*" * 20)
print("La sumatoria de números pares del 1 al 1000 es:", sumaLista(listado))

"""
6# Escribir un programa que reciba una lista de números enteros y devuelva la lista ordenada de forma ascendente.
"""
listadoDes = [5,8,6,1,4,9,2,7,3]

def ordenaLista(listado: list) -> int:
  orden = sorted(listado)
  return orden

print("\n" + "*" * 20 + " Ejercicio 06 " + "*" * 20)
print("La lista ordenada de:", listadoDes, "es:", ordenaLista(listadoDes))

"""
7# Escribir un programa que pida al usuario un número entero y muestre por pantalla el triángulo de Pascal correspondiente a ese número.
"""
def pascal():
  numFila = input("Favor ingresa un número de filas para triangulo de Pascal: ")
  numFila = int(numFila)

  for i in range(1, numFila + 1):
    for j in range(0, numFila - i + 1):
      print(' ', end='')

    # primer elemento siempre es 1
    column = 1
    for j in range(1, i+1):

      # primer valor de linea siempre es 1
      print(' ', column, sep='', end='')

      # usando coeficiente binominal
      column = column * (i - j) // j
    print()
    
print("\n" + "*" * 20 + " Ejercicio 07 " + "*" * 20)
pascal()

"""
8# Escribir un programa que lea un archivo de texto y cuente la cantidad de palabras que contiene.
"""
def contarPalabras(nombreArchivo: str):
  file = open(nombreArchivo,'r')
  palabras = file.read()
  listaPalabras = (palabras).split()
  print("Archivo indicado contiene:", len(listaPalabras), "palabras")
  file.close()

print("\n" + "*" * 20 + " Ejercicio 08 " + "*" * 20)
contarPalabras('file.txt')

"""
9# Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla la frecuencia de cada letra.
"""
def frecuenciaLetras(cadena: list) -> None:
  frecuenciaLetra = []
  newCadena = list(cadena) # separar cada letra como una lista
  for letra in newCadena:
    if ((letra, newCadena.count(letra))) not in frecuenciaLetra: # determinar si existe dentro de 'frecuenciaLetra'
      frecuenciaLetra.append((letra, newCadena.count(letra)))

  return frecuenciaLetra

print("\n" + "*" * 20 + " Ejercicio 09 " + "*" * 20)
palabra = 'paralelepipedo'
print("Frecuencia para la palabra:", palabra, '\n', frecuenciaLetras(palabra))
print("\n" + "*" * 54 + "\n")

"""
10# Escribir un programa que implemente el juego del ahorcado.
El programa debe pedir al usuario que adivine una palabra secreta,
dando pistas sobre la misma y mostrando el progreso del usuario en su intento de adivinarla.
"""

import random

escenario = \
'''   
~~~~~~~~~|~
         |
 0123456 J    
~~~~~~~~~~~   
'''

simbolos = '><(((º>'

def bienvenida():
  print('*' * 73)
  print('* Te doy la bienvenida al juego del ahorcado de Billy[<Programador>] :) *')
  print('*' * 73)

# paso 1
def inicializar_juego(diccionario):
  palabra = random.choice(diccionario).lower()
  tablero = ['_'] * len(palabra)
  return tablero, palabra, []

# paso 2
def mostrar_escenario(errores):
  escena = escenario
  for i in range(0, len(simbolos)):
    simbolo = simbolos[i] if i < errores else ' '
    escena = escena.replace(str(i), simbolo)
  print(escena)

# paso 3
def mostrar_tablero(tablero, letras_erroneas):
  for casilla in tablero:
    print(casilla, end=' ')
  print()
  print()
  if len(letras_erroneas) > 0:
    print('Letras erróneas:', *letras_erroneas)
    print()

# paso 4
def pedir_letra(tablero, letras_erroneas):
  valida = False
  while not valida:
    letra = input('Introduce una letra (a-z): ').lower()
    valida = 'a' <= letra <= 'z' and len(letra) == 1 # es una letra
    if not valida:
      print('Error, la letra tiene que estar entre a y z.')
    else:
      valida = letra not in tablero + letras_erroneas
      if not valida:
        print('Letra repetida, prueba con otra.')
  return letra

# paso 5
def procesar_letra(letra, palabra, tablero, letras_erroneas):
  if letra in palabra:
    print('¡Muy bien! Has acertado una letra.')
    actualizar_tablero(letra, palabra, tablero)
  else:
    print('¡Oh! Has fallado.')
    letras_erroneas.append(letra)

# paso 5 (auxiliar)
def actualizar_tablero(letra, palabra, tablero):
  for indice, letra_palabra in enumerate(palabra):
    if letra == letra_palabra:
      tablero[indice] = letra

# paso 6
def comprobar_palabra(tablero):
  return '_' not in tablero

# bucle principal de juego
def jugar_al_ahorcado(diccionario):
  tablero, palabra, letras_erroneas = inicializar_juego(diccionario)  # paso 1
  while len(letras_erroneas) < len(simbolos):  # pasos 7 y 8
    mostrar_escenario(len(letras_erroneas))  # paso 2
    mostrar_tablero(tablero, letras_erroneas)  # paso 3
    letra = pedir_letra(tablero, letras_erroneas)  # paso 4
    procesar_letra(letra, palabra, tablero, letras_erroneas)  # paso 5
    if comprobar_palabra(tablero):  # paso 6
      print('¡Perfecto, lo has logrado!')
      break
  else:
    print(f'¡Lo siento! ¡Has perdido! La palabra a adivinar era {palabra}.')
    mostrar_escenario(len(letras_erroneas))  # paso 7

  mostrar_tablero(tablero, letras_erroneas)

def jugar_otra_vez():
  return input('Deseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ')

def despedida():
  print('*' * 73)
  print('* Gracias por jugar al ahorcado de Billy[<Programador>]. ¡Hasta pronto! *')
  print('*' * 73)


if __name__ == '__main__':

  diccionario = ['mansion', 'pescado', 'calamar', 'verdura', 'pajaro']

bienvenida()
while True:
  jugar_al_ahorcado(diccionario)
  if jugar_otra_vez() != 's': break
despedida()