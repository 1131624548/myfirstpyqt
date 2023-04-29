import sys
from PyQt6.QtCore import QSize,Qt 
from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        
        super()._init_()
        self.setWindowTitle("DIP System")
        self.setFixedSize(QSize(1000,500))
        button=QPushButton("YOLOv5")
        self.setCentralWidget(button)

app=QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
