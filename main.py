"""
Proyecto programado 2
Melanie Parra Valverde (2024239734)
Carlos Hernandez Calderon (2024283448)
"""
import os
import sys
import gui
from mapManager import createMap
from readCSV import readCSV
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy



os.system('cls')

def createWindow():
    class MainWindow(QMainWindow):
        def __init__(self):
            coordinatesMatrix, adyacencyMatrix = readCSV()
            super().__init__()
            self.setWindowTitle("Mapa Interactivo")
            self.setFixedSize(1280, 720)
            
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
            self.setWindowIcon(QIcon(icon_path))

            self.setStyleSheet("background-color: #F2EFE9;") 

            self.centralWidget = QWidget(self)
            self.setCentralWidget(self.centralWidget)

            mainLayout = QHBoxLayout()

            self.menuButton = QPushButton("☰")
            self.menuButton.setFixedSize(40, 40)
            self.menuButton.setStyleSheet("""
                QPushButton {
                    font-size: 24px;
                    background-color: #FFB6C1;
                    border: none;
                    color: white;
                    border-radius: 20px;
                }
                QPushButton:hover {
                    background-color: #FF99A1;
                }
                QPushButton:pressed {
                    background-color: #FF7F89;
                }
            """)
            self.menuButton.clicked.connect(self.toggleButtons)


            titleLabel = QLabel("Mapa\nInteractivo")
            titleLabel.setObjectName("titleLabel")
            titleLabel.setAlignment(Qt.AlignCenter)
            titleLabel.setWordWrap(True)
            titleLabel.setStyleSheet("""
                QLabel#titleLabel {
                    font-size: 24px;
                    font-weight: bold;
                    color: #FF99A1;
                    background-color: transparent;
                    margin: 2px;
                }
            """)
            titleLabel.setFixedHeight(100)

 
            self.buttonsLayout = QVBoxLayout()
            self.buttonsLayout.setSpacing(10)
            self.buttonsLayout.setContentsMargins(20, 20, 20, 20)


            self.buttonsLayout.addWidget(titleLabel, alignment=Qt.AlignTop)

            self.buttons = [
                self.createButton("Agregar Coordenadas", self.addCoordinatesButtonFunc),
                self.createButton("Actualizar Coordenadas", print),
                self.createButton("Eliminar Coordenadas", self.deleteCoordinatesButtonFunc),
                self.createButton("Mostrar Matriz", gui.showMatrixGUI),
                self.createButton("Calcular Camino Más Corto", print),
                self.createButton("Guardar", print),
            ]


            self.buttonsLayout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
            for button in self.buttons:
                self.buttonsLayout.addWidget(button)
            self.buttonsLayout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

            self.buttonsContainer = QWidget()
            self.buttonsContainer.setLayout(self.buttonsLayout)
            self.buttonsContainer.setVisible(False)


            mapLayout = QVBoxLayout()
            self.web_view = QWebEngineView(self)
            createMap(coordinatesMatrix, adyacencyMatrix)
            direction = os.path.dirname(os.path.abspath(__file__))
            htmlPath = os.path.join(direction, "./Map.html")
            self.web_view.setUrl(QUrl.fromLocalFile(htmlPath))
            mapLayout.setContentsMargins(10, 10, 10, 10)
            mapLayout.addWidget(self.web_view)


            menuLayout = QVBoxLayout()
            menuLayout.addWidget(self.menuButton, alignment=Qt.AlignTop)
            menuLayout.addWidget(self.buttonsContainer, alignment=Qt.AlignTop)

            mainLayout.addLayout(menuLayout)
            mainLayout.addLayout(mapLayout)

            mainLayout.setStretchFactor(menuLayout, 1)
            mainLayout.setStretchFactor(mapLayout, 4)

            self.centralWidget.setLayout(mainLayout)

        def createButton(self, text, action):
            button = QPushButton(text)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFB6C1;
                    border: none;
                    color: white;
                    padding: 10px 20px;
                    font-size: 16px;
                    margin: 14px 10px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #FF99A1;
                }
                QPushButton:pressed {
                    background-color: #FF7F89;
                }
            """)
            button.clicked.connect(action) 
            return button

        def toggleButtons(self):
            isVisible = self.buttonsContainer.isVisible()
            self.buttonsContainer.setVisible(not isVisible)
            
        def updateMap(self):
          coordinatesMatrix, adyacencyMatrix = readCSV()
          createMap(coordinatesMatrix, adyacencyMatrix)
          direction = os.path.dirname(os.path.abspath(__file__))
          htmlPath = os.path.join(direction, "./Map.html")
          self.web_view.setUrl(QUrl.fromLocalFile(htmlPath))
          
        def addCoordinatesButtonFunc(self):
          gui.addCoordinatesGUI()
          self.updateMap()

        """
        Las otras funciones
        """
        def deleteCoordinatesButtonFunc(self) : #Aqui se le pasa por parámetro el objeto, osea la ventana por así decirlo, la clase jsdjkls
            gui.deleteCoordinatesGUI() #Invoca la función que aún no hacemos para eliminar jskd
            self.updateMap() #Actualiza el mapa
          

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
createWindow()



'''


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
    createMap(coordinatesMatrix, adyacencyMatrix)
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
  
'''
