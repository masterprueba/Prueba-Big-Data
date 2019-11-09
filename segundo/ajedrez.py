import numpy as np

#Metodo principal.
def jugar(x,y,pieza):
  if x >= 0 and x < 8 and y >= 0 and y < 8:
    a = [[0] * 8 for i in range(8)]  
    if pieza=="caballo":
      print(caballo(x,y,a))
    elif pieza=="reina":
      print(reina(x,y,a))
    elif pieza=="alfil":
      print(alfil(x,y,a))
    elif pieza=="torre":
      print(torre(x,y,a))
    elif pieza=="rey":
      print(rey(x,y,a))
    else:
      print("pieza no creada")
  else:
    print("Posicion X o Y fuera del rango (rango = 0 a 7)")

def caballo(x,y,a):
  for i in range(8):
    for j in range(8):
        if i == x and j == y:
            a[i][j] = 8
        elif i == x+1 and j == y+2:
            a[i][j] = 1
        elif i == x+1 and j == y-2:
            a[i][j] = 1
        elif i == x+2 and j == y+1:
            a[i][j] = 1
        elif i == x+2 and j == y-1:
            a[i][j] = 1
        elif i == x-1 and j == y+2:
            a[i][j] = 1
        elif i == x-1 and j == y-2:
            a[i][j] = 1
        elif i == x-2 and j == y+1:
            a[i][j] = 1
        elif i == x-2 and j == y-1:
            a[i][j] = 1
        else:
            a[i][j] = 0
  return np.asarray(a)

def reina(x,y,a):
  for i in range(8):
    for j in range(8):
      if i == x and j == y:
            a[i][j] = 8
      elif i == x :
            a[i][j] = 1
      elif j == y :
            a[i][j] = 1
      elif j+i == x+y :
            a[i][j] = 1
      elif i-j == x-y :
            a[i][j] = 1
      else:
            a[i][j] = 0
  return np.asarray(a)

def alfil(x,y,a):  
  for i in range(8):
    for j in range(8):
      if i == x and j == y:
            a[i][j] = 8
      elif j+i == x+y :
            a[i][j] = 1
      elif i-j == x-y :
            a[i][j] = 1
      else:
            a[i][j] = 0
  return np.asarray(a)

def torre(x,y,a):  
  for i in range(8):
    for j in range(8):
      if i == x and j == y:
            a[i][j] = 8
      elif i == x :
            a[i][j] = 1
      elif j == y :
            a[i][j] = 1
      else:
            a[i][j] = 0
  return np.asarray(a)

def rey(x,y,a): 
  for i in range(8):
    for j in range(8):
      if i == x and j == y:
          a[i][j] = 8
      elif i == (x-1) and j == y:
        a[i][j] = 1
      elif i == (x+1) and j == y:
        a[i][j] = 1
      elif i == x and j == (y+1):
        a[i][j] = 1
      elif i == x and j == (y-1):
        a[i][j] = 1
      else:
            a[i][j] = 0
  return np.asarray(a)

jugar(2,5,"reina")

