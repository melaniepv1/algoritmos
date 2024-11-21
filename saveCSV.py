import pandas as pd

'''
Entradas:
Salidas:
Restricciones:
'''

def saveCSV(coordinatesMatrix, adyacencyMatrix):
    coordinatesHeader = ['Name', 'Latitude', 'Longitude', 'Color']
    coordinatesMatrix = [coordinatesHeader] + coordinatesMatrix
    coordinatesPath = "./Data/ncoordinatesMatrix.csv"
    df_coordinates = pd.DataFrame(coordinatesMatrix)
    df_coordinates.to_csv(coordinatesPath, index=False, header=False)

    adyacencyFirstRow = []
    
    for coord in coordinatesMatrix:
        adyacencyFirstRow.append(coord[0])
    
    for id, row in enumerate(adyacencyMatrix):
        adyacencyMatrix[id] = [coordinatesMatrix[id+1][0]] + row
        
    adyacencyMatrix = [adyacencyFirstRow] + adyacencyMatrix        
    adyacencyPath = "./Data/nadyacencyMatrix.csv"
    df_adyacency = pd.DataFrame(adyacencyMatrix)
    df_adyacency.to_csv(adyacencyPath, index=False, header=False)
