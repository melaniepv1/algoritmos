import folium

def createMap(coordinatesMatrix, adyacencyMatrix):

    if coordinatesMatrix:
        center = coordinatesMatrix[0][1:3]
    else:
        center = [0, 0]  

    map = folium.Map(location=center, zoom_start=16)

 
    for i, coords in enumerate(coordinatesMatrix):
        folium.Marker(location=coords[1:3], popup=coords[0], icon=folium.Icon(color='black',icon_color=coords[3], icon="bookmark")).add_to(map)
        for j, connection in enumerate(adyacencyMatrix[i]):
            if connection != 0 and i < j:
                lineCords = [coords[1:3], coordinatesMatrix[j][1:3]]
                folium.PolyLine(locations=lineCords, color="#888888", weight=2, opacity = 0.6).add_to(map)


    map.save("Map.html")


