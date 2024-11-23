import haversine as hs
from haversine import Unit
'''
def calculateDistance 

Entradas:
    - coordinatesMatrix (Matriz)
      [nombre, latitud, longitud, color], latitud y longitud son float.
    - adyacencyMatrix (Matriz)

Salidas:
    - distanceMatrix (Matriz): Una matriz que representa las distancias entre edificios conectados.

Restricciones:
    - En coordinatesMatrix, cada elemento debe tener al menos tres elementos [nombre, latitud, longitud].
    - adyacencyMatrix: Debe ser una matriz cuadrada.
'''


def calculateDistance(coordinatesMatrix, adyacencyMatrix):
  distanceMatrix = [[float("inf")] * len(adyacencyMatrix)
                    for row in range(len(adyacencyMatrix))]
  for x, row in enumerate(adyacencyMatrix):
    for y, value in enumerate(row):
      if value == 1:
        distance = hs.haversine(coordinatesMatrix[x][1:3],
                                coordinatesMatrix[y][1:3],
                                unit=Unit.METERS)
        distanceMatrix[x][y] = distance
  return distanceMatrix
