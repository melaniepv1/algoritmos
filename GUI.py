from PyQt5.QtGui import QColor, QIcon
import coordinatesManager as cm
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QColorDialog, QScrollArea, QWidget, QCheckBox, QGridLayout
from readCSV import readCSV
from saveCSV import saveCSV
import os




def addCoordinatesGUI():
    dialog = QDialog()
    dialog.setWindowTitle("Agregar Coordenadas")
    dialog.setFixedSize(600, 300)
    iconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
    dialog.setWindowIcon(QIcon(iconPath))

    mainLayout = QVBoxLayout()

    formLayout = QVBoxLayout()

    nameLabel = QLabel("Nombre:")
    nameLabel.setStyleSheet("""
                            QLabel{
                                font-size: 16px;
                                color:#FF99A1
                            }
                            """)
    nameInput = QLineEdit()
    nameInput.setStyleSheet("""
        QLineEdit {
            font-size: 16px;
            padding: 5px;
            border-radius: 8px;
            background-color: #FFB6C1;
            color: white;
        }
        QLineEdit:focus {
            background-color: #FF99A1;
        }
    """)
    formLayout.addWidget(nameLabel)
    formLayout.addWidget(nameInput)

    latLabel = QLabel("Latitud:")
    latLabel.setStyleSheet("""
                            QLabel{
                                font-size: 16px;
                                color:#FF99A1
                            }
                            """)
    latInput = QLineEdit()
    latInput.setStyleSheet("""
        QLineEdit {
            font-size: 16px;
            padding: 5px;
            border-radius: 8px;
            background-color: #FFB6C1;
            color: white;
        }
        QLineEdit:focus {
            background-color: #FF99A1;
        }
    """)
    formLayout.addWidget(latLabel)
    formLayout.addWidget(latInput)

    lonLabel = QLabel("Longitud:")
    lonLabel.setStyleSheet("""
                            QLabel{
                                font-size: 16px;
                                color:#FF99A1
                            }
                            """)
    lonInput = QLineEdit()
    lonInput.setStyleSheet("""
        QLineEdit {
            font-size: 16px;
            padding: 5px;
            border-radius: 8px;
            background-color: #FFB6C1;
            color: white;
        }
        QLineEdit:focus {
            background-color: #FF99A1;
        }
    """)
    formLayout.addWidget(lonLabel)
    formLayout.addWidget(lonInput)

    buttonsLayout = QHBoxLayout()

    colorButton = QPushButton("Seleccionar Color")
    colorButton.setStyleSheet("""
        QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF99A1;
        }
        QPushButton:pressed {
            background-color: #FF7F89;
        }
    """)
    buttonsLayout.addWidget(colorButton)

    colorDisplay = QLabel()
    colorDisplay.setFixedSize(30, 30) 
    colorDisplay.setStyleSheet("""
        QLabel {
            background-color: #FFFFFF;
            border: 1px solid #FF99A1;
            font-size: 16px;
            color: #FF99A1;
            border-radius: 8px;
        }
    """)
    buttonsLayout.addWidget(colorDisplay)

    selectedColor = QColor(120, 120, 120)

    def openColorDialog():
        nonlocal selectedColor
        color = QColorDialog.getColor()
        if color.isValid():
            selectedColor = color
            colorDisplay.setStyleSheet(f"""
                QLabel {{
                    background-color: {color.name()};
                    border: 1px solid #FF99A1;
                    font-size: 16px;
                    color: #FF99A1;
                    border-radius: 8px;
                }}
            """)

    colorButton.clicked.connect(openColorDialog)

    acceptButton = QPushButton("Aceptar")
    acceptButton.setStyleSheet("""
        QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF99A1;
        }
        QPushButton:pressed {
            background-color: #FF7F89;
        }
    """)
    buttonsLayout.addWidget(acceptButton)


    cancelButton = QPushButton("Cancelar")
    cancelButton.setStyleSheet("""
        QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF99A1;
        }
        QPushButton:pressed {
            background-color: #FF7F89;
        }
    """)
    buttonsLayout.addWidget(cancelButton)


    def acceptData():
        name = nameInput.text()
        latitude = latInput.text()
        longitude = lonInput.text()
        if name and latitude and longitude:
            coordinatesMatrix, adyacencyMatrix = readCSV()
            newCoordinates = [name, latitude, longitude, selectedColor.name()]
            print(adyacencyMatrix[0], "Se aceptó agregar Coordenadas")
            nCoordinatesMatrix, nAdyacencyMatrix = cm.addCoordinates(newCoordinates, coordinatesMatrix, adyacencyMatrix)
            print(nAdyacencyMatrix[0], "Se instancio nAdyacencia")
            adyacencyList = getAdyacencyList(nCoordinatesMatrix)
            
            nAdyacencyMatrix = cm.addAdyacency(adyacencyMatrix, (len(adyacencyMatrix)-1), adyacencyList)
            print(nAdyacencyMatrix[0],"Se agregó la adyacencia")
            saveCSV(nCoordinatesMatrix, nAdyacencyMatrix)
            print(nAdyacencyMatrix[0], "Se guardó")
            
            dialog.accept()
        

    acceptButton.clicked.connect(acceptData)

    cancelButton.clicked.connect(dialog.reject)

    mainLayout.addLayout(formLayout)
    mainLayout.addLayout(buttonsLayout)

    dialog.setLayout(mainLayout)
    dialog.exec_()
    
def getAdyacencyList(nCoordinatesMatrix):
    dialog = QDialog()
    dialog.setWindowTitle("Agregar Adyacencias")
    dialog.setFixedSize(450, 500)
    iconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
    dialog.setWindowIcon(QIcon(iconPath))
    mainLayout = QVBoxLayout()
    
    instructionsLabel = QLabel("Seleccione las coordenadas adyacentes:")
    instructionsLabel.setStyleSheet("""
        QLabel {
            font-size: 16px;
            color: #FF99A1;
        }
    """)
    mainLayout.addWidget(instructionsLabel)
    
    scrollArea = QScrollArea()
    scrollArea.setWidgetResizable(True)
    scrollWidget = QWidget()
    scrollLayout = QVBoxLayout()

    checkboxes = []
    for index, coordinate in enumerate(nCoordinatesMatrix[:-1]):
        checkbox = QCheckBox(f"{coordinate[0]} (Índice: {index})")
        checkbox.setStyleSheet("""
            QCheckBox {
                spacing: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
            QCheckBox::indicator:unchecked {
                border: 2px solid #FFB6C1; 
                background: #FFFFFF; 
                border-radius: 4px;
                }
            QCheckBox::indicator:unchecked:hover {
                border-color: #FF99A1; 
            }
            QCheckBox::indicator:checked {
                border: 2px solid #FF99A1; 
                background: #FFB6C1; 
                border-radius: 4px; 
            }
        """)
        checkboxes.append((index, checkbox))
        scrollLayout.addWidget(checkbox)
    
    scrollWidget.setLayout(scrollLayout)
    scrollArea.setWidget(scrollWidget)
    mainLayout.addWidget(scrollArea)
    
    buttonsLayout = QHBoxLayout()

    acceptButton = QPushButton("Aceptar")
    acceptButton.setStyleSheet("""
        QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF99A1;
        }
        QPushButton:pressed {
            background-color: #FF7F89;
        }
    """)

    cancelButton = QPushButton("Cancelar")
    cancelButton.setStyleSheet("""
        QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF99A1;
        }
        QPushButton:pressed {
            background-color: #FF7F89;
        }
    """)
    
    buttonsLayout.addWidget(cancelButton)
    buttonsLayout.addWidget(acceptButton)

    def acceptSelection():
        selectedIndices = []
        for index, checkbox in checkboxes:
            if checkbox.isChecked(): selectedIndices.append(index)
        dialog.selectedIndices = selectedIndices  
        dialog.accept()

    acceptButton.clicked.connect(acceptSelection)
    cancelButton.clicked.connect(dialog.reject)

    mainLayout.addLayout(buttonsLayout)

    dialog.setLayout(mainLayout)
    
    if dialog.exec_() == QDialog.Accepted:
        return dialog.selectedIndices
    return []

def showMatrixGUI():
    dialog = QDialog()
    dialog.setWindowTitle("Show Matrix")
    dialog.setFixedSize(600, 120)
    iconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
    dialog.setWindowIcon(QIcon(iconPath))
    
    mainLayout = QHBoxLayout()
    
    ShowCoordinatesMatrixButton = QPushButton("Show Coordinates")
    ShowCoordinatesMatrixButton.setStyleSheet("""
        QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF99A1;
        }
        QPushButton:pressed {
            background-color: #FF7F89;
        }
    """)

    ShowAdyacencyMatrixButton = QPushButton("Show Adyacency")
    ShowAdyacencyMatrixButton.setStyleSheet("""
        QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF99A1;
        }
        QPushButton:pressed {
            background-color: #FF7F89;
        }
    """)
    
    def showCoordinatesMatrix():
        dialog = QDialog()
        dialog.setWindowTitle("Coordinates")
        dialog.setFixedSize(900, 720)
        iconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
        dialog.setWindowIcon(QIcon(iconPath))
        
        mainLayout = QHBoxLayout()
        
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollWidget = QWidget()
        scrollLayout = QGridLayout()
        
        nameLabel = QLabel("Name")
        nameLabel.setStyleSheet("""
                            QLabel{
                                font-size: 16px;
                                background-color: #FFB6C1;
                                border: none;
                                color: white;
                                padding: 10px 20px;
                                border-radius: 8px;
                                text-align: center;
                            }
                            """)
        nameLabel.setFixedHeight(40)
        
        latLabel = QLabel("Latitude")
        latLabel.setStyleSheet("""
                            QLabel{
                                font-size: 16px;
                                background-color: #FFB6C1;
                                border: none;
                                color: white;
                                padding: 10px 20px;
                                border-radius: 8px;
                            }
                            """)
        
        lonLabel = QLabel("Longitude")
        lonLabel.setStyleSheet("""
                            QLabel{
                                font-size: 16px;
                                background-color: #FFB6C1;
                                border: none;
                                color: white;
                                padding: 10px 20px;
                                border-radius: 8px;
                            }
                            """)       
        
        colorLabel = QLabel("Color")
        colorLabel.setStyleSheet("""
                            QLabel{
                                font-size: 16px;
                                background-color: #FFB6C1;
                                border: none;
                                color: white;
                                padding: 10px 20px;
                                border-radius: 8px;
                            }
                            """)      
        
        scrollLayout.addWidget(nameLabel,0,0)
        scrollLayout.addWidget(latLabel,0,1)
        scrollLayout.addWidget(lonLabel,0,2)
        scrollLayout.addWidget(colorLabel,0,3)   
        
        coordinatesMatrix, adyacencyMatrix = readCSV()
        
        for idRow, row in enumerate(coordinatesMatrix):
            for idCol, text in enumerate(row):
                label = QLabel(str(text))
                scrollLayout.addWidget(label, idRow+1, idCol)
            
        
        
        
        scrollWidget.setLayout(scrollLayout)
        scrollArea.setWidget(scrollWidget)
        
        mainLayout.addWidget(scrollArea)
        
        dialog.setLayout(mainLayout)
        dialog.exec_()
        
    def showAdyacencyMatrix():
        coordinatesMatrix, adyacencyMatrix = readCSV()
        dialog = QDialog()
        dialog.setWindowTitle("Coordinates")
        dialog.setFixedSize(900, 720)
        iconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
        dialog.setWindowIcon(QIcon(iconPath))
        
        mainLayout = QHBoxLayout()
        
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollWidget = QWidget()
        scrollLayout = QGridLayout()
        
        nameLabel = QLabel("Name")
        nameLabel.setStyleSheet("""
                            QLabel{
                                font-size: 16px;
                                background-color: #FFB6C1;
                                border: none;
                                color: white;
                                padding: 10px 20px;
                                border-radius: 4px;
                            }
                            """)
        
        nameLabel.setFixedHeight(40)
        
        scrollLayout.addWidget(nameLabel, 0, 0)
        
        for index, coord in enumerate(coordinatesMatrix):
            labelH = QLabel(coord[0]) 
            labelH.setStyleSheet("""
                            QLabel{
                                font-size: 16px;
                                background-color: #FFB6C1;
                                border: none;
                                color: white;
                                padding: 10px 20px;
                                border-radius: 4px;
                            }
                            """)
            labelV = QLabel(coord[0])
            labelV.setStyleSheet(labelH.styleSheet())
            
            scrollLayout.addWidget(labelH, 0, index+1)
            scrollLayout.addWidget(labelV, index+1, 0)
            
        for idRow, row in enumerate(adyacencyMatrix):
            for idCol, adyacency in enumerate(row):
                label = QLabel(str(adyacency))
                label.setStyleSheet("""
                                    QLabel{
                                font-size: 16px;
                                background-color: #DDDDDD;
                                padding: 10px 20px;
                                border-radius: 4px;
                            }
                                    """)
                scrollLayout.addWidget(label, idRow+1, idCol+1)
        
        scrollWidget.setLayout(scrollLayout)
        scrollArea.setWidget(scrollWidget)
        
        mainLayout.addWidget(scrollArea)
        
        dialog.setLayout(mainLayout)
        dialog.exec_()
    
    ShowCoordinatesMatrixButton.clicked.connect(showCoordinatesMatrix)
    ShowAdyacencyMatrixButton.clicked.connect(showAdyacencyMatrix)
    
    mainLayout.addWidget(ShowCoordinatesMatrixButton)
    mainLayout.addWidget(ShowAdyacencyMatrixButton)
    
    
    
    dialog.setLayout(mainLayout)
    dialog.exec_()


def deleteCoordinatesGUI():
    dialog = QDialog()
    dialog.setWindowTitle("Delete Coordinates")
    dialog.setFixedSize(500, 600)
    iconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
    dialog.setWindowIcon(QIcon(iconPath))


    mainLayout = QVBoxLayout()

    instructionsLabel = QLabel("Seleccione las coordenadas a eliminar:")
    instructionsLabel.setStyleSheet("""
        QLabel {
            font-size: 16px;
            color: #FF99A1;
        }
    """)
    mainLayout.addWidget(instructionsLabel)

    scrollArea = QScrollArea()
    scrollArea.setWidgetResizable(True)
    scrollWidget = QWidget()
    scrollLayout = QVBoxLayout()
    coordinatesMatrix, adyacencyMatrix = readCSV()

    checkboxes = []
    for index, coordinate in enumerate(coordinatesMatrix):
        checkbox = QCheckBox(f"{coordinate[0]} (Índice: {index})")
        checkbox.setStyleSheet("""
            QCheckBox {
                spacing: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
            QCheckBox::indicator:unchecked {
                border: 2px solid #FFB6C1; 
                background: #FFFFFF; 
                border-radius: 4px;
            }
            QCheckBox::indicator:unchecked:hover {
                border-color: #FF99A1; 
            }
            QCheckBox::indicator:checked {
                border: 2px solid #FF99A1; 
                background: #FFB6C1; 
                border-radius: 4px; 
            }
        """)
        checkboxes.append((index, checkbox))
        scrollLayout.addWidget(checkbox)

    scrollWidget.setLayout(scrollLayout)
    scrollArea.setWidget(scrollWidget)
    mainLayout.addWidget(scrollArea)

    buttonsLayout = QHBoxLayout()

    acceptButton = QPushButton("Eliminar")
    acceptButton.setStyleSheet("""
        QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF99A1;
        }
        QPushButton:pressed {
            background-color: #FF7F89;
        }
    """)
    cancelButton = QPushButton("Cancelar")
    cancelButton.setStyleSheet("""
        QPushButton {
            background-color: #FFB6C1;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #FF99A1;
        }
        QPushButton:pressed {
            background-color: #FF7F89;
        }
    """)
    buttonsLayout.addWidget(cancelButton)
    buttonsLayout.addWidget(acceptButton)

    def acceptSelection():
        selectedIndices = [index for index, checkbox in checkboxes if checkbox.isChecked()]
        if selectedIndices:
            coordinatesMatrix, adyacencyMatrix = readCSV()
            for index in selectedIndices:
                coordinatesMatrix, adyacencyMatrix = cm.deleteCoordinates(coordinatesMatrix, adyacencyMatrix, index)
            saveCSV(coordinatesMatrix, adyacencyMatrix)
        dialog.accept()

    acceptButton.clicked.connect(acceptSelection)
    cancelButton.clicked.connect(dialog.reject)

    mainLayout.addLayout(buttonsLayout)
    dialog.setLayout(mainLayout)


    dialog.exec_()