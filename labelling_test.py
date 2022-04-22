import os
import sys
from time import sleep
import numpy as np

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPixmap 
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QWidget,
)

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.index_image = 0
        self.int = 35000 + self.index_image
        self.image_file = '/home/alexandreabela/Downloads/35000/'+f'{self.int}'+'.png'
        self.labels = []
        self.number_of_examples = 1000
        self.attribute = 'Narrow_Eyes'
        self.setupUi()

    def setupUi(self):
        
        self.setWindowTitle(f'{self.attribute}')
        self.resize(700, 550)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        # Create and connect widgets

        self.image_label = QLabel(f"Image : {self.index_image}/{self.number_of_examples}", self)
        self.image_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.Btn1 = QPushButton("Ans : 0", self)
        self.Btn1.clicked.connect(self.first_answer)

        self.Btn2 = QPushButton("Ans : 1", self)
        self.Btn2.clicked.connect(self.second_answer)

        self.Btn3 = QPushButton("Ans : 2", self)
        self.Btn3.clicked.connect(self.third_answer)

        self.Btn4 = QPushButton("Ans : 3", self)
        self.Btn4.clicked.connect(self.fourth_answer)

        self.Btn5 = QPushButton("Ans : 4", self)
        self.Btn5.clicked.connect(self.fifth_answer)

        self.ReturnBtn = QPushButton("Return", self)
        self.ReturnBtn.clicked.connect(self.return_to_previous_image)

        self.SaveBtn = QPushButton("Save", self)
        self.SaveBtn.clicked.connect(self.save_results)

        self.qpixmap = QPixmap(f'{self.image_file}')
        self.image = QLabel(self)
        self.image.setPixmap(self.qpixmap)

        # Set the layout
        layout = QHBoxLayout()

        layout.addWidget(self.image)
        layout.addWidget(self.image_label)
        layout.addWidget(self.Btn1)
        layout.addWidget(self.Btn2)
        layout.addWidget(self.Btn3)
        layout.addWidget(self.Btn4)
        layout.addWidget(self.Btn5)
        layout.addWidget(self.ReturnBtn)
        layout.addWidget(self.SaveBtn)
        
        self.centralWidget.setLayout(layout)

    def first_answer(self):
        
        self.index_image += 1
        self.labels.append(0)

        if self.index_image == self.number_of_examples : 
            self.image_label.setText('Attention plus d image disponible')
        
        else :  
            self.int = 35000 + self.index_image
            self.image_file = '/home/alexandreabela/Downloads/35000/'+f'{self.int}'+'.png'

            self.qpixmap = QPixmap(f'{self.image_file}')
            self.image.setPixmap(self.qpixmap)

            self.image_label.setText(f'Image : {self.index_image}/{self.number_of_examples}')
    
    def second_answer(self): 
        self.index_image += 1
        self.labels.append(1)
        if self.index_image == self.number_of_examples : 
            self.image_label.setText('Attention plus d image disponible')
            
        else : 
            self.int = 35000 + self.index_image
            self.image_file = '/home/alexandreabela/Downloads/35000/'+f'{self.int}'+'.png'

            self.qpixmap = QPixmap(f'{self.image_file}')
            self.image.setPixmap(self.qpixmap)

            self.image_label.setText(f'Image : {self.index_image}/{self.number_of_examples}')

    def third_answer(self):
        
        self.index_image += 1
        self.labels.append(2)

        if self.index_image == self.number_of_examples : 
            self.image_label.setText('Attention plus d image disponible')
        
        else :  
            self.int = 35000 + self.index_image
            self.image_file = '/home/alexandreabela/Downloads/35000/'+f'{self.int}'+'.png'

            self.qpixmap = QPixmap(f'{self.image_file}')
            self.image.setPixmap(self.qpixmap)

            self.image_label.setText(f'Image : {self.index_image}/{self.number_of_examples}')

    def fourth_answer(self):
        
        self.index_image += 1
        self.labels.append(3)

        if self.index_image == self.number_of_examples : 
            self.image_label.setText('Attention plus d image disponible')
        
        else :  
            self.int = 35000 + self.index_image
            self.image_file = '/home/alexandreabela/Downloads/35000/'+f'{self.int}'+'.png'

            self.qpixmap = QPixmap(f'{self.image_file}')
            self.image.setPixmap(self.qpixmap)

            self.image_label.setText(f'Image : {self.index_image}/{self.number_of_examples}')
    
    def fifth_answer(self):
        
        self.index_image += 1
        self.labels.append(4)

        if self.index_image == self.number_of_examples : 
            self.image_label.setText('Attention plus d image disponible')
        
        else :  
            self.int = 35000 + self.index_image
            self.image_file = '/home/alexandreabela/Downloads/35000/'+f'{self.int}'+'.png'

            self.qpixmap = QPixmap(f'{self.image_file}')
            self.image.setPixmap(self.qpixmap)

            self.image_label.setText(f'Image : {self.index_image}/{self.number_of_examples}')
    
    def return_to_previous_image(self):
        self.index_image -= 1
        self.labels.pop()
        self.int = 35000 + self.index_image
        self.image_file = '/home/alexandreabela/Downloads/35000/'+f'{self.int}'+'.png'

        self.qpixmap = QPixmap(f'{self.image_file}')
        self.image.setPixmap(self.qpixmap)

        self.image_label.setText(f'Image : {self.index_image}/{self.number_of_examples}')
    
    def save_results(self):
        self.labels = np.asarray(self.labels)
        np.save(f'/home/alexandreabela/Desktop/{self.attribute}.npy',self.labels) 
        l = np.load(f'/home/alexandreabela/Desktop/{self.attribute}.npy')
        if len(l) == self.number_of_examples:
            print("Filed save ok")
        
app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())