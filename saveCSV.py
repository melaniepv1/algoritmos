import pandas as pd

'''
Entradas:
Salidas:
Restricciones:
'''

def saveCSV(coordinatesMatrix, adyacencyMatrix):
    coordinatesPath = "./Data/coordinatesMatrix.csv"
    df_coordinates = pd.DataFrame(coordinatesMatrix)
    df_coordinates.to_csv(coordinatesPath, index=False, header=False)

    adyacencyPath = "./Data/adyacencyMatrix.csv"
    df_adyacency = pd.DataFrame(adyacencyMatrix)
    df_adyacency.to_csv(adyacencyPath, index=False, header=False)