'''
Entradas:
Salidas:
Restricciones:
'''


def addCoordinates(newCoordinates, coordinatesMatrix, adyacencyMatrix):
  coordinatesMatrix.append(newCoordinates)
  adyacencyMatrix.append([0] * (len(coordinatesMatrix) - 1))
  for row in adyacencyMatrix:
    row.append(0)
  return coordinatesMatrix, adyacencyMatrix


def addAdyacency(adyacencyMatrix, newCoordinatesIndex, adyacencyList):
  for adyacency in adyacencyList:
    adyacencyMatrix[newCoordinatesIndex][adyacency] = 1
    adyacencyMatrix[adyacency][newCoordinatesIndex] = 1
  return adyacencyMatrix


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
Entradas:
Salidas:
Restricciones:
'''


def deleteCoordinates(coordinatesMatrix, adyacencyMatrix, index):
  del coordinatesMatrix[index]
  del adyacencyMatrix[index]

  for row in adyacencyMatrix:
    del row[index]

  return coordinatesMatrix, adyacencyMatrix




'''
Entradas:
Salidas:
Restricciones:
'''
def updateDeleteAdyacency(adyacencyMatrix, index):
  for x in range(len(adyacencyMatrix)):
      adyacencyMatrix[index][x] = float("inf")
      adyacencyMatrix[x][index] = float("inf")
  return adyacencyMatrix