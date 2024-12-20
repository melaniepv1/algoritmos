import pandas as pd

'''
Entradas:
    - coordinatesMatrix (Matriz)
    - adyacencyMatrix (Matriz)

Salidas:
    - Guarda los datos en archivos CSV.

Restricciones:
    - coordinatesMatrix debe contener al menos una fila de encabezado con los campos 'Name', 'Latitude', 'Longitude', 'Color'.
    - Los valores en la matriz `adyacencyMatrix` deben ser numéricos.
'''


def saveCSV(coordinatesMatrix, adyacencyMatrix):
    coordinatesHeader = ['Name', 'Latitude', 'Longitude', 'Color']
    coordinatesMatrix = [coordinatesHeader] + coordinatesMatrix
    coordinatesPath = "./Data/coordinatesMatrix.csv"
    df_coordinates = pd.DataFrame(coordinatesMatrix)
    df_coordinates.to_csv(coordinatesPath, index=False, header=False)

    adyacencyFirstRow = []
    
    for coord in coordinatesMatrix:
        adyacencyFirstRow.append(coord[0])
    
    for id, row in enumerate(adyacencyMatrix):
        adyacencyMatrix[id] = [coordinatesMatrix[id+1][0]] + row
        
    adyacencyMatrix = [adyacencyFirstRow] + adyacencyMatrix        
    adyacencyPath = "./Data/adyacencyMatrix.csv"
    df_adyacency = pd.DataFrame(adyacencyMatrix)
    df_adyacency.to_csv(adyacencyPath, index=False, header=False)