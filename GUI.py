import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
import os
from coordinatesManager import addAdyacency, addCoordinates, updateAdyacency, deleteCoordinates
from calculateDistance import calculateDistance
from saveCSV import saveCSV
from shortestPath import dijsktra



def createWindow():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Map")
            self.setFixedSize(1280, 720)

            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
            self.setWindowIcon(QIcon(icon_path))

            title_label = QLabel("Mapa\ninteractivo", self)
            title_label.setStyleSheet("""
                font-size: 24px;
                font-weight: bold;
                color: #FF99A1;
                padding: 20px;
            """)
            title_label.setAlignment(Qt.AlignCenter)
            title_label.setWordWrap(True)

            title_label.setMinimumWidth(260)

            title_layout = QVBoxLayout()
            title_layout.addWidget(title_label)
            title_layout.setAlignment(Qt.AlignCenter)
            
            title_layout.setContentsMargins(20, 20, 20, 20)


            self.centralWidget = QWidget(self)
            self.setCentralWidget(self.centralWidget)


            mainLayout = QHBoxLayout()

            buttonsLayout = QVBoxLayout()
            topSpacer = QWidget()
            topSpacer.setFixedHeight(30)            # Para ajustar la altura de los botones
            buttonsLayout.addWidget(topSpacer)

            addCoordsButton = self.createButton("Agregar Coordenadas")
            updateCoordsButton = self.createButton("Actualizar Coordenadas")
            deleteCoordsButton = self.createButton("Eliminar Coordenadas")
            showMatrixButton = self.createButton("Mostrar matriz")
            showShortestPathButton = self.createButton("Calcular camino más corto")
            saveCSVButton = self.createButton("Guardar")
            
            
            buttonsLayout.addWidget(addCoordsButton)
            buttonsLayout.addWidget(updateCoordsButton)
            buttonsLayout.addWidget(deleteCoordsButton)
            buttonsLayout.addWidget(showMatrixButton)
            buttonsLayout.addWidget(showShortestPathButton)
            buttonsLayout.addWidget(saveCSVButton)
            

            # Aqui va el mapa 


            mapLayout = QVBoxLayout()

            self.web_view = QWebEngineView(self)
            direction = os.path.dirname(os.path.abspath(__file__))
            htmlPath = os.path.join(direction, "./Map.html")
            self.web_view.setUrl(QUrl.fromLocalFile(htmlPath))

            
            mapLayout.addWidget(self.web_view)
            
            mainLayout.addLayout(buttonsLayout)
            mainLayout.addLayout(mapLayout) 
            
            mainLayout.setStretchFactor(buttonsLayout, 1)
            mainLayout.setStretchFactor(mapLayout, 4) 


            self.centralWidget.setLayout(mainLayout)

        def createButton(self, text):
            button = QPushButton(text)
            button.setStyleSheet("""
                QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s;
        }
        QPushButton:hover {                              /* Cuando se pasa el cursor sobre el boton */
            background-color: #FF99A1;
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        }
        QPushButton:pressed {                           /* Cuando se presiona el boton */
            background-color: #FF7F89;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);  
        }
    """)
            return button 

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    createWindow()
