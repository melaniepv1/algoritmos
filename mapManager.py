from readCSV import readCSV
import folium





'''
def createMap(coordinatesMatrix, adyacencyMatrix)

Entradas:
        - coordinatesMatrix (Matriz)
        - adyacencyMatrix (Matriz)
Salidas:
        - Crea un archivo `Map.html` que muestra un mapa interactivo con los nodos y sus conexiones.

Restricciones:
        - No hay
'''
def createMap(coordinatesMatrix, adyacencyMatrix):
    if coordinatesMatrix:
        centerLat = sum(coords[1] for coords in coordinatesMatrix) / len(coordinatesMatrix)
        centerLon = sum(coords[2] for coords in coordinatesMatrix) / len(coordinatesMatrix)
        center = [centerLat, centerLon]
    else:
        center = [0, 0]

    map = folium.Map(location=center, zoom_start=17)

    for i, coords in enumerate(coordinatesMatrix):
        folium.Marker(location=coords[1:3], popup=coords[0], icon=folium.Icon(color='black', icon_color=coords[3], icon="bookmark")).add_to(map)
        for j, connection in enumerate(adyacencyMatrix[i]):
            if connection != 0 and i < j:
                lineCords = [coords[1:3], coordinatesMatrix[j][1:3]]
                folium.PolyLine(locations=lineCords, color="#888888", weight=2, opacity=0.6).add_to(map)

    folium.LatLngPopup().add_to(map)
    map.save("Map.html")



'''
def showShortestPath(path, coordinatesMatrix, adyacencyMatrix)

Entradas:
        - path (List)
        - coordinatesMatrix (Matriz)
        - adyacencyMatrix (Matriz)

Salidas:
        - Muestra el camino mas corto entre dos nodos en el Map.html

Restricciones:
        - El camino debe ser una lista de índices válidos en la matriz de coordenadas.
'''
def showShortestPath(path, coordinatesMatrix, adyacencyMatrix):

    shortestPathCoords = []
    for index in path:
        coords = [coordinatesMatrix[index][1], coordinatesMatrix[index][2]]
        shortestPathCoords.append(coords)

    if coordinatesMatrix:
        centerLat = sum(coords[1] for coords in coordinatesMatrix) / len(coordinatesMatrix)
        centerLon = sum(coords[2] for coords in coordinatesMatrix) / len(coordinatesMatrix)
        center = [centerLat, centerLon]
    else:
        center = [0, 0]

    map = folium.Map(location=center, zoom_start=17)

    for i, coords in enumerate(coordinatesMatrix):
        if i in path:
            folium.Marker(location=coords[1:3], popup=coords[0], icon=folium.Icon(color='black', icon_color=coords[3], icon="bookmark")).add_to(map)

    folium.PolyLine(shortestPathCoords, color="#FFB6C1", weight=4, opacity=1).add_to(map)

    folium.LatLngPopup().add_to(map)

    map.save("Map.html")


