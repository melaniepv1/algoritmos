import pandas as pd
'''
def readCSV(path)
Entradas:

Salidas:

Restricciones:
'''


def readCSV():

  coordinatesPath = "./Data/ncoordinatesMatrix.csv"
  df = pd.read_csv(coordinatesPath)
  coordinatesMatrix = df.values.tolist()

  adyacencyPath = "./Data/nadyacencyMatrix.csv"
  df = pd.read_csv(adyacencyPath)
  adyacencyMatrix = df.values.tolist()

  for index, rows in enumerate(adyacencyMatrix):
    adyacencyMatrix[index] = rows[1:]

  return coordinatesMatrix, adyacencyMatrix
