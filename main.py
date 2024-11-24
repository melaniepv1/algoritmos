
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        coordinatesMatrix, adyacencyMatrix = readCSV()
        
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
            self.createButton("Calcular Camino Más Corto", self.shortestPathButtonFunc),
            self.createButton("Agregar Coordenadas", self.addCoordinatesButtonFunc),
            self.createButton("Actualizar Coordenadas", self.updateCoordinatesButtonFunc),
            self.createButton("Eliminar Coordenadas", self.deleteCoordinatesButtonFunc),
            self.createButton("Desconectar Coordenada", self.disconnectCoordinatesButtonFunc),
            self.createButton("Mostrar Matriz", gui.showMatrixGUI),
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

        self.reloadButton = QPushButton("↻")
        self.reloadButton.setFixedSize(50,50)
        self.reloadButton.setStyleSheet("""
    QPushButton{
        font-size: 24px;
        color: white;
        font-weight: bold;
        background-color: #FFB6C1;
        border: none;
        border-radius: 25px;
    }
    QPushButton:hover{
        background-color: #FF99A1;                                    
    }
    QPushButton:pressed {
        background-color: #FF7F89;
    }
""")
        self.reloadButton.clicked.connect(self.updateMap)
        self.reloadButton.setGeometry(self.width() - 70,20,50,50)
        self.reloadButton.setParent(self)

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

    def deleteCoordinatesButtonFunc(self):
        gui.deleteCoordinatesGUI()
        self.updateMap()

    def updateCoordinatesButtonFunc(self) :
        gui.updateCoordinatesGUI()
        self.updateMap()

    def shortestPathButtonFunc(self):
        gui.findShortestPathGUI()
        direction = os.path.dirname(os.path.abspath(__file__))
        htmlPath = os.path.join(direction, "./Map.html")
        self.web_view.setUrl(QUrl.fromLocalFile(htmlPath))

    def disconnectCoordinatesButtonFunc(self):
        gui.disconnectCoordinatesGUI()
        self.updateMap()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
