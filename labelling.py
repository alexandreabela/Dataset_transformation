import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Main_Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
  
        # creation du bouton
        self.button1 = QPushButton("Oui")
        self.button2 = QPushButton("Non")

        # on connecte le signal "clicked" a la methode appui_bouton
        self.button1.clicked.connect(self.postive_answer)
        self.button2.clicked.connect(self.negative_answer)
 
        # creation du gestionnaire de mise en forme
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

        self.setWindowTitle("Labelling")

        label = QLabel(self)

    def postive_answer(self):
        print("Oui")

    def negative_answer(self): 
        print("Non")

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
    
fen = Main_Window()
fen.show()

app.exec_()