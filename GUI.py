import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

def createWindow():
    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow).__init__()
            self.setWindowTitle("a")
            self.setFixedSize(800, 600)
    
    app = QApplication(sys.argv)
    sys.exit(app.exec_())

    return app