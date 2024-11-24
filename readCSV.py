import pandas as pd

'''
Entradas:
    - No hay.

Salidas:
    - coordinatesMatrix (Matriz): Matriz de coordenadas leída desde el archivo CSV.
    - adyacencyMatrix (Matriz): Matriz de adyacencia leída desde el archivo CSV.

Restricciones:
    - Los archivos CSV `coordinatesMatrix.csv` y `adyacencyMatrix.csv` deben existir en la carpeta `./Data/`.
'''



def readCSV():

  coordinatesPath = "./Data/coordinatesMatrix.csv"
  df = pd.read_csv(coordinatesPath)
  coordinatesMatrix = df.values.tolist()

  adyacencyPath = "./Data/adyacencyMatrix.csv"
  df = pd.read_csv(adyacencyPath)
  adyacencyMatrix = df.values.tolist()

  for index, rows in enumerate(adyacencyMatrix):
    adyacencyMatrix[index] = rows[1:]

  return coordinatesMatrix, adyacencyMatrix
