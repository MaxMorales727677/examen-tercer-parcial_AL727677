import math

array = None
res1 = None
b = None
item = None
n = None
bloque = None
a = None
previo = None
contar = None
res = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

# Describe this function...
def min2(res1, b):
  global array, item, n, bloque, a, previo, contar, res
  if b > a:
    res1 = a
  else:
    res1 = b
  return res1


array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
item = float(text_prompt('Ingrese el número a buscar: '))
n = 16
bloque = round(math.sqrt(n))
previo = 1
contar = 1
while array[int(min2(bloque, n) - 1)] < item:
  previo = bloque
  bloque = bloque + round(math.sqrt(n))
  contar = contar + 1
  if previo >= n:
    res = -1
while array[int(previo - 1)] < item:
  previo = previo + 1
  if array[int(previo - 1)] == item:
    res = previo
  else:
    res = -1
if res >= 0:
  if res == 0:
    res = 1
    print('El número ' + str(item))
    print(' fue encontrado en la posición ' + str(res))
    print(' con ' + str(contar))
    print(' saltos de búsqueda')
  else:
    print('El número ' + str(item))
    print(' fue encontrado en la posición ' + str(res))
    print(' con ' + str(contar))
    print(' saltos de búsqueda')
else:
  print('Se realizaron ' + str(contar))
  print(' saltos para buscar el número ' + str(item))
  print(' en el arreglo con longitud ' + str(n))
  print(', pero no fue encontrado')