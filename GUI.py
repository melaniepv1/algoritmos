from PyQt5.QtGui import QColor, QIcon
from shortestPath import dijsktra
import coordinatesManager as cm
from calculateDistance import calculateDistance
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QColorDialog, QScrollArea, QWidget, QCheckBox, QGridLayout, QComboBox
from readCSV import readCSV
from saveCSV import saveCSV
from mapManager import showShortestPath
import os



'''
def addCoordinatesGUI()

Entradas:
        - No hay, los datos son proporcionados a través de la interfaz gráfica.

Salidas:
        - Crea un cuadro de diálogo donde el usuario puede ingresar los datos, que luego serán utilizados en otras partes del programa.

Restricciones:
        - Los campos de entrada para nombre, latitud y longitud deben contener valores válidos.
        - El color seleccionado debe ser válido y debe actualizarse en la interfaz.
'''
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



    '''
    def openColorDialog()

    Entradas:
        - No hay, la selección del color se realiza mediante el cuadro de diálogo.

    Salidas:
        - El color seleccionado se actualiza en la interfaz de usuario.

    Restricciones:
        - El color seleccionado debe ser válido.
    '''
    
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



    '''
    def acceptData()

    Entradas:
            - name (str)
            - latitude (str)
            - longitude (str)
            - selectedColor (QColor)

    Salidas:
            - Los datos se agregan a las matrices de coordenadas y adyacencia, y se guardan en un archivo CSV.

    Restricciones:
            - El nombre, latitud y longitud no pueden estar vacios.
            - El color seleccionado debe ser un valor válido de QColor.
    '''

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


"""
def getAdyacencyList(nCoordinatesMatrix)

Entradas:
    - nCoordinatesMatrix (matriz)

Salidas:
    - Una lista de listas de valores booleanos donde cada valor indica si una coordenada es adyacente a otra.

Restricciones:
    - nCoordinatesMatrix debe ser una lista no vacía de coordenadas.
    - El índice de cada coordenada debe ser único.
"""
    
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

    '''
    def acceptSelection()

    Entradas:
            - checkboxes (lista de tuplas)
            - acceptButton (QPushButton)
            - cancelButton (QPushButton)
            - dialog (QDialog)

    Salidas:
            - Una lista de índices de los `checkboxes` que están seleccionados.

    Restricciones:
            - `dialog` debe ser una instancia de `QDialog` y debe tener el atributo `selectedIndices` para almacenar los índices seleccionados.
    '''
    
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


'''
def showMatrixGUI()

Entradas:
    - La función configura un diálogo y botones de la interfaz de usuario.

Salidas:
    - Un diálogo con el título  que contiene dos botones (`ShowCoordinatesMatrixButton` y `ShowAdyacencyMatrixButton`).

Restricciones:
    - No hay.

'''

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
    


    '''
    def showCoordinatesMatrix()

    Entradas:
        - La función utiliza datos leídos de los archivos CSV.
        
    Salidas:
        - Un diálogo con un área desplazable que contiene una matriz con los valores de las coordenadas leídas desde `coordinatesMatrix`.
        
    Restricciones:
        - No hay.

    '''

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
        


    '''
    def showAdyacencyMatrix()

    Entradas:
        - La función utiliza datos leídos de los archivos CSV.
        
    Salidas:
        - Un diálogo con un área desplazable que contiene una matriz que muestra los nombres de las coordenadas y los valores de la matriz de adyacencia.
        
    Restricciones:
        - No hay.

    '''

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




'''
def deleteCoordinatesGUI()

Entradas:
    - La función utiliza datos leídos de los archivos CSV.
    
Salidas:
    - Un diálogo con un área desplazable que contiene una lista para seleccionar las coordenadas que el usuario desea eliminar. 
    - Un botón "Eliminar" para ejecutar la acción de eliminar las coordenadas seleccionadas y un botón "Cancelar" para cerrar el diálogo sin realizar cambios.
    
Restricciones:
    - No hay.

'''

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
            font-weight: bold;
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




    '''
    def acceptSelection()

    Entradas:
            - La función utiliza una lista `checkboxes`, que contiene las casillas de verificación para las coordenadas.
            
    Salidas:
            - La función elimina las coordenadas seleccionadas de `coordinatesMatrix` y `adyacencyMatrix`, luego guarda los cambios en los archivos CSV mediante `saveCSV()`.
            
    Restricciones:
            - No hay.

    '''
    def acceptSelection():
        selectedIndices = [index for index, checkbox in checkboxes if checkbox.isChecked()]
        selectedIndices.sort(reverse=True)
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


'''
def updateCoordinatesGUI()

Entradas:
    - La función utiliza datos leídos de los archivos CSV.
    
Salidas:
    - Un diálogo (`QDialog`) con una interfaz de usuario para actualizar las coordenadas:
        - Una lista para seleccionar coordenadas.
        - Campos de texto para modificar el nombre, latitud y longitud de la coordenada seleccionada.
        - Un botón para seleccionar un color.
    
Restricciones:
    - No hay.

'''

def updateCoordinatesGUI():
    dialog = QDialog()
    dialog.setWindowTitle("Update Coordinates")
    dialog.setFixedSize(500, 600)
    iconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
    dialog.setWindowIcon(QIcon(iconPath))


    mainLayout = QVBoxLayout()

    instructionsLabel = QLabel("Seleccione las coordenadas a actualizar:")
    instructionsLabel.setStyleSheet("""
        QLabel {
            font-size: 16px;
            font-weight: bold;
            color: #FF99A1;
        }
    """)
    mainLayout.addWidget(instructionsLabel)

    formLayout = QVBoxLayout()

    coordinateMatrix, _ = readCSV()

    dropDownList = QComboBox()
    for coords in coordinateMatrix:
        dropDownList.addItem(coords[0])

    formLayout.addWidget(dropDownList)

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


    '''
    def openColorDialog()

    Entradas:
        - No hay, la selección del color se realiza mediante el cuadro de diálogo.

    Salidas:
        - El color seleccionado se actualiza en la interfaz de usuario.

    Restricciones:
        - El color seleccionado debe ser válido.
    '''

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

    '''
    def acceptSelection()

    Entradas:
            - coordinatesMatrix (matriz)
            - adyacencyMatrix (matriz)
            - index (int)
            - name (str)
            - latitude (str)
            - longitude (str)
            - selectedColor (QColor)

    Salidas:
            - Se actualiza la coordenada seleccionada en `coordinatesMatrix` con los nuevos valores y se guarda la matriz actualizada junto con `adyacencyMatrix`.

    Restricciones:
            - No hay.


    '''

    def acceptSelection():
        coordinatesMatrix, adyacencyMatrix = readCSV()
        index = dropDownList.currentIndex()
        name = nameInput.text()
        latitude = latInput.text()
        longitude = lonInput.text()

        if name and latitude and longitude:
            newCoordinates = [name, latitude, longitude, selectedColor.name()]
            coordinatesMatrix[index] = newCoordinates
            saveCSV(coordinatesMatrix, adyacencyMatrix)
        dialog.accept()

    acceptButton.clicked.connect(acceptSelection)
    cancelButton.clicked.connect(dialog.reject)

    mainLayout.addLayout(formLayout)
    mainLayout.addLayout(buttonsLayout)
    dialog.setLayout(mainLayout)


    dialog.exec_()



'''
def findShortestPathGUI()

Entradas:
    - coordinatesMatrix (Matriz).
    - adyacencyMatrix (Matriz)
    - startComboBox (QComboBox)
    - endComboBox (QComboBox)
    - iconPath (str)

Salidas:
    - Un cuadro de diálogo donde el usuario puede seleccionar el punto de inicio y el punto de destino mediante los `QComboBox`.

Restricciones:
    - No hay.

'''


def findShortestPathGUI():

    coordinatesMatrix, adyacencyMatrix = readCSV()

    dialog = QDialog()
    dialog.setWindowTitle("Show Shortest Path")
    dialog.setFixedSize(400, 180)
    iconPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./icon.ico")
    dialog.setWindowIcon(QIcon(iconPath))

    mainLayout = QVBoxLayout()

    instructionsLabel = QLabel("Seleccione el inicio y el final")
    instructionsLabel.setStyleSheet("""
        QLabel {
            font-size: 12px;
            font-weight: bold;
            color: #FF99A1;
            text-align: center;
        }
    """)
    mainLayout.addWidget(instructionsLabel)

    comboBoxLayout = QHBoxLayout()

    startLabel = QLabel("Inicio: ")
    startComboBox = QComboBox()
    endLabel = QLabel("Final: ")
    endComboBox = QComboBox()

    for coords in coordinatesMatrix:
        startComboBox.addItem(coords[0])
        endComboBox.addItem(coords[0])

    comboBoxLayout.addWidget(startLabel)
    comboBoxLayout.addWidget(startComboBox)
    comboBoxLayout.addWidget(endLabel)
    comboBoxLayout.addWidget(endComboBox)

    mainLayout.addLayout(comboBoxLayout)



    '''
    def acceptSelection()

    Entradas:
        - coordinatesMatrix (Matriz)
        - adyacencyMatrix (Matriz)
        - startComboBox (QComboBox)
        - endComboBox (QComboBox)
        - acceptButton (QPushButton)

    Salidas:
        - Se llama a la función `dijkstra` para calcular el camino más corto entre los puntos seleccionados.
        - Se llama a la función `showShortestPath` para mostrar el resultado del cálculo del camino más corto.

    Restricciones:
        - No hay.

    '''

    def acceptSelection():

        distanceMatrix = calculateDistance(coordinatesMatrix, adyacencyMatrix)

        start = startComboBox.currentIndex()
        end = endComboBox.currentIndex()

        path, distance = dijsktra(distanceMatrix, start, end)

        showShortestPath(path, coordinatesMatrix, adyacencyMatrix)

        dialog.accept()
            



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
    acceptButton.clicked.connect(acceptSelection)
    mainLayout.addWidget(acceptButton)


    dialog.setLayout(mainLayout)
    dialog.exec_()