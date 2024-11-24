'''
def addCoordinates(newCoordinates, coordinatesMatrix, adyacencyMatrix)

Entradas:  
        - newCoordinates (list)
        - coordinatesMatrix (matriz)
        - adyacencyMatrix (matriz)
Salidas:  
        - coordinatesMatrix (matriz): Matriz de coordenadas con la nueva coordenada agregada.  
        - adyacencyMatrix (matriz): Matriz de adyacencias con las conexiones correspondientes a la nueva coordenada.  
Restricciones:  
        - La matriz de coordenadas y la de adyacencias deben tener el mismo tamaño antes de agregar una nueva coordenada.  

'''

def addCoordinates(newCoordinates, coordinatesMatrix, adyacencyMatrix):
  coordinatesMatrix.append(newCoordinates)
  adyacencyMatrix.append([0] * (len(coordinatesMatrix) - 1))
  for row in adyacencyMatrix:
    row.append(0)
  return coordinatesMatrix, adyacencyMatrix

'''
def addAdyacency(adyacencyMatrix, newCoordinatesIndex, adyacencyList)

Entradas:  
        - adyacencyMatrix (matriz)  
        - newCoordinatesIndex (int)  
        - adyacencyList (list)  
Salidas:  
        - adyacencyMatrix (matriz): Matriz de adyacencias con las nuevas conexiones para el índice especificado.  
Restricciones:  
        - La matriz debe ser cuadrada.  
        - El índice `newCoordinatesIndex` debe ser válido dentro del rango de la matriz. 
'''

def addAdyacency(adyacencyMatrix, newCoordinatesIndex, adyacencyList):
  for adyacency in adyacencyList:
    adyacencyMatrix[newCoordinatesIndex][adyacency] = 1
    adyacencyMatrix[adyacency][newCoordinatesIndex] = 1
  return adyacencyMatrix

'''
def updateAdyacency(adyacencyMatrix, index, adyacencyList)

Entradas:  
        - adyacencyMatrix (matriz)  
        - index (int)  
        - adyacencyList (list)  
Salidas:  
        - adyacencyMatrix (matriz): Matriz de adyacencias con las nuevas conexiones para el índice especificado.  
Restricciones:  
        - La matriz debe ser cuadrada.  
        - El índice debe ser válido dentro del rango de la matriz.  
''' 

def updateAdyacency(adyacencyMatrix, index, adyacencyList):
  for x, _ in enumerate(adyacencyMatrix):
    if x in adyacencyList:
      adyacencyMatrix[index][x] = 1
      adyacencyMatrix[x][index] = 1
    else:
      adyacencyMatrix[index][x] = 0
      adyacencyMatrix[x][index] = 0

  return adyacencyMatrix


'''
def deleteCoordinates(coordinatesMatrix, adyacencyMatrix, index)

Entradas:
        - coordinatesMatrix (Matriz)
        - adyacencyMatrix (Matriz)
        - index (int)
Salidas:
        - coordinatesMatrix (matriz): Matriz de coordenadas con el nodo eliminado.
        - adyacencyMatrix (matriz): Matriz de adyacencias con las conexiones del nodo eliminado.
Restricciones:
        - La matriz debe ser cuadrada.
        - El índice debe ser válido dentro del rango de la matriz.
'''

def deleteCoordinates(coordinatesMatrix, adyacencyMatrix, index):
  del coordinatesMatrix[index]
  del adyacencyMatrix[index]

  for row in adyacencyMatrix:
    del row[index]

  return coordinatesMatrix, adyacencyMatrix




'''
def updateDeleteAdyacency(adyacencyMatrix, index)

Entradas: 
        - adyacencyMatrix  (matriz)
        - index (int)
Salidas:
        - adyacencyMatrix  (matriz): Matriz actualizada donde las conexiones del nodo especificado se han eliminado.
Restricciones:
        - La matriz debe ser cuadrada.
        - El índice debe ser válido dentro del rango de la matriz.
'''
def updateDeleteAdyacency(adyacencyMatrix, index):
  for x in range(len(adyacencyMatrix)):
      adyacencyMatrix[index][x] = float("inf")
      adyacencyMatrix[x][index] = float("inf")
  return adyacencyMatrix


def disconectCoords(index, adyacencyMatrix):
        for i, _ in enumerate(adyacencyMatrix):
                adyacencyMatrix[i][index] = 0
                adyacencyMatrix[index][i] = 0
        return adyacencyMatrix
                
