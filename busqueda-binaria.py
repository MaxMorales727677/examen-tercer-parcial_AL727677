import math

n = None
bandera = None
start = None
final = None
array = None
x = None
middle = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


n = 12
bandera = False
start = 1
final = n
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
x = float(text_prompt('Ingrese el elemento a buscar:'))
while bandera == False and start <= final:
  middle = round((start + final) / 2)
  if x == array[int(middle - 1)]:
    bandera = True
  else:
    if x < array[int(middle - 1)]:
      final = middle - 1
    else:
      start = middle + 1
if bandera == True:
  print('El valor buscado ' + str(x))
  print('Se encuentra en la posición del índice ' + str(middle))
else:
  print('El valor buscado ' + str(x))
  print('No fue localizado en el arreglo de ' + str(n))
  print('Posiciones.')