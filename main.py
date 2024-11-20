"""
Proyecto programado 2
Melanie Parra Valverde (2024239734)
Carlos Hernandez Calderon (2024283448)
"""
import sys
from calculateDistance import calculateDistance 
from readCSV import readCSV
from shortestPath import dijsktra
from mapManager import createMap
from saveCSV import saveCSV
import numpy as np 
import coordinatesManager as cm
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import os


coordinatesMatrix, adyacencyMatrix = readCSV()
distanceMatrix = calculateDistance(coordinatesMatrix, adyacencyMatrix)
createMap(coordinatesMatrix, adyacencyMatrix)



class MapViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mapa del Campus")
        self.setGeometry(100, 100, 800, 600)

        self.web_view = QWebEngineView(self)

        direction = os.path.dirname(os.path.abspath(__file__))
        htmlPath = os.path.join(direction, "Map.html")
        self.web_view.setUrl(QUrl.fromLocalFile(htmlPath))

        self.setCentralWidget(self.web_view)



while (True):

  print("1. Agregar Coordenadas")
  print("2. Actualizar Coordenadas")
  print("3. Eliminar Coordenadas")
  print("4. Mostrar matriz")
  print("5. Ver mapa")
  print("6. Calcular camino más corto")
  print("7. Guardar")
  print("8. Salir")


  opc = int(input("Ingrese una opcion: "))

  if opc == 1:
    newCoordinates = []
    newCoordinates.append(input("Ingrese el nombre de la coordenada: "))
    newCoordinates.append(float(
        input("Ingrese la latitud de la coordenada: ")))
    newCoordinates.append(
        float(input("Ingrese la longitud de la coordenada: ")))
    newCoordinates.append('#888888')  
    coordinatesMatrix, adyacencyMatrix = cm.addCoordinates(
        newCoordinates, coordinatesMatrix, adyacencyMatrix)
    print("Coordenada agregada")

    adyacencyList = input(
        "Ingrese los indices de las coordenadas adyacentes separados por comas: "
    )
    adyacencyList = adyacencyList.split(",")
    adyacencyList = [int(x) for x in adyacencyList]

    adyacencyMatrix = cm.addAdyacency(adyacencyMatrix,
                                      len(coordinatesMatrix) - 1,
                                      adyacencyList)
    print("Adyacencia agregada")

  elif opc == 2:
    print("Ingrese el indice de la coordenada que desea actualizar")
    index = int(input())
    print("Ingrese el nombre de la coordenada")
    newCoordinates = []
    newCoordinates.append(input())
    print("Ingrese la latitud de la coordenada")
    newCoordinates.append(float(input()))
    print("Ingrese la longitud de la coordenada")
    newCoordinates.append(float(input()))

    coordinatesMatrix[index] = newCoordinates

    adyacencyList = input(
        "Ingrese los indices de las coordenadas adyacentes separados por comas: "
    )
    adyacencyList = adyacencyList.split(",")
    adyacencyList = [int(x) for x in adyacencyList]
    adyacencyMatrix = cm.updateAdyacency(adyacencyMatrix, index, adyacencyList)

  elif opc == 3:
    buildingIndex = int(input("Ingresa el índice del edificio a eliminar: "))
    coordinatesMatrix, adyacencyMatrix = cm.deleteCoordinates(
        coordinatesMatrix, adyacencyMatrix, buildingIndex)
    print("Edificio eliminado correctamente.")
  elif opc == 4:
    coordinatesMatrixNP = np.array(coordinatesMatrix)
    print(coordinatesMatrixNP)
    adyacencyMatrixNP = np.array(adyacencyMatrix)
    print(adyacencyMatrixNP)
  elif opc == 5:
    app = QApplication(sys.argv)
    viewer = MapViewer()
    viewer.show()
    app.exec_()  
  elif opc == 6:
    start = int(input("Ingrese el nodo de inicio: "))
    end = int(input("Ingrese el nodo de destino: "))
    if start < 0 or start >= len(coordinatesMatrix) or end < 0 or end >= len(coordinatesMatrix):
        print("Índices inválidos. Intente nuevamente.")
    else:
        path, distance = dijsktra(adyacencyMatrix, start, end)
        
        if distance == float("inf"):
            print("No hay camino entre los nodos.")
        else:
            print(f"El camino más corto entre {start} y {end} es: {path}")
            print(f"La distancia es: {distance}")
  elif opc == 7:
    saveCSV(coordinatesMatrix, adyacencyMatrix)
    pass
  elif opc == 8:
    break
  
