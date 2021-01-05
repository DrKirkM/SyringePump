# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:01:31 2020

@author: kirk.mutafopulos

"""

import sys
import serial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Pumps(QMainWindow): 
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):    
        #layout=QFormLayout()
        
        #Start Pump Button
        btn1 = QPushButton("Run Pump 1", self)
        btn1.move(30, 140)
        btn1.resize(200,32)
        
        #Stop Pump Button
        btn2 = QPushButton("Stop Pump 1", self)
        btn2.move(250, 140)
        btn2.resize(200,32)
        
        #Setting FLOW Value
        '''
        lineEdit1 = QLineEdit()
        lineEdit1.move(500,500)
        lineEdit1.resize(200,200)
        '''
        
        #Set Flow Rate Button for mL/hour
        btn3 = QPushButton("Set to mL/hour", self)
        btn3.move(470, 140)
        btn3.resize(200,32)
        
        #Set Diameter Value
        '''
        lineEdit2 = QlineEdit()
        lineEdit2.move(500,500)
        lineEdit2.resize(200,200)
        '''
        #Set Syringe Diameter Button        
        btn4 = QPushButton("Set Diameter (mm)", self)
        btn4.move(690, 140)
        btn4.resize(200,32)
        
        #Set Flow Rate Button for uL/hour
        btn5 = QPushButton("Set to uL/hour", self)
        btn5.move(470,180)
        btn5.resize(200,32)
      
        #Set Flow Rate Button for uL/min
        btn6 = QPushButton("Set to uL/min", self)
        btn6.move(470, 220)
        btn6.resize(200,32)
        
        # Run Pump for address 01
        btn7 = QPushButton("Run Pump 2", self)
        btn7.move(30,320)
        btn7.resize(200,32)
        
        #Stop Pump for address 01
        btn8 = QPushButton("Stop Pump 2", self)
        btn8.move(250,320)
        btn8.resize(200, 32)
        
        #Set flow rate to mL/hr for address 01
        btn9 = QPushButton("Set to mL/hour", self)
        btn9.move(470,320)
        btn9.resize(200,32)
        
        #Set Diameter (mm) for Pump address 01
        btn10 = QPushButton("Set Diameter (mm)", self)
        btn10.move(690,320)
        btn10.resize(200,32)
        
        #Set flow rate to ul/hour for pump address 01
        btn11 = QPushButton("Set to uL/hour", self)
        btn11.move(470,360)
        btn11.resize(200,32)
        
        #Set flow Rate to ul/min for pump address 01
        btn12 = QPushButton("Set to uL/min", self)
        btn12.move(470,400)
        btn12.resize(200,32)
        
        #Run Pump for address 02
        btn13 =  QPushButton("Run Pump 3", self)
        btn13.move(30, 500)
        btn13.resize(200,32)
        
        #Stop Pump for address 02
        btn14 = QPushButton("Stop Pump 3", self)
        btn14.move(250,500)
        btn14.resize(200,32)
        
        #Set flow rate to mL/hr for pump address 02
        btn15 = QPushButton("Set to mL/hour", self)
        btn15.move(470,500)
        btn15.resize(200,32)
        
        #Set flow rate to ul/hour for pump address 02
        btn16 = QPushButton("Set to uL/hour", self)
        btn16.move(470,540)
        btn16.resize(200,32)
        
        #Set flow rate to ul/min for pump address 02
        btn17 = QPushButton("Set to uL/min", self)
        btn17.move(470,580)
        btn17.resize(200,32)
        
        #Set Diameter (mm) for Pump address 02
        btn18 = QPushButton("Set Diameter (mm)", self)
        btn18.move(690,500)
        btn18.resize(200,32)
        
        #Stop all pumps
        btn19 = QPushButton("STOP ALL PUMPS", self)
        btn19.move(100,620)
        btn19.resize(200,32)
        
        #Run all pumps
        btn20 = QPushButton("RUN ALL PUMPS", self)
        btn20.move(100,570)
        btn20.resize(200,32)
        
        DiamInfo = QLabel("Syringe Diameter: 1mL=4.78mm, 3mL=8.66mm, 5mL=12.06mm, 10mL=14.5mm, 20mL=19.13mm, 30mL=21.7mm" , self)
        DiamInfo.move(80,700)
        DiamInfo.resize(850,32)
        
        ProgInfo = QLabel("This program was made by K. Mutafopulos, PhD", self)
        ProgInfo.move(80,730)
        ProgInfo.resize(850,32)
        
        btn1.clicked.connect(self.runbuttonClicked)            
        btn2.clicked.connect(self.stopbuttonClicked)
        btn3.clicked.connect(self.sfrbuttonClicked)
        btn4.clicked.connect(self.diambuttonClicked)
        btn5.clicked.connect(self.ulhbuttonClicked)
        btn6.clicked.connect(self.ulmbuttonClicked)
        btn7.clicked.connect(self.run2buttonClicked)
        btn8.clicked.connect(self.stop2buttonClicked)
        btn9.clicked.connect(self.mlh2buttonClicked)
        btn10.clicked.connect(self.diam2buttonClicked)
        btn11.clicked.connect(self.ulh2buttonClicked)
        btn12.clicked.connect(self.ulm2buttonClicked)
        btn13.clicked.connect(self.run3buttonClicked)
        btn14.clicked.connect(self.stop3buttonClicked)
        btn15.clicked.connect(self.mlh3buttonClicked)
        btn16.clicked.connect(self.ulh3buttonClicked)
        btn17.clicked.connect(self.ulm3buttonClicked)
        btn18.clicked.connect(self.diam3buttonClicked)
        btn19.clicked.connect(self.stopallbuttonClicked)
        btn20.clicked.connect(self.runallbuttonClicked)
        
        #
        # MRB: QLineEdit Instance
        #Input Flow Rate Value for Pump Address 00
        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.setObjectName("frEdit") # Flow-Rate Edit
        self.lineEdit1.setText(" Input flow rate")# Placeholder text
        self.lineEdit1.resize(200, 32)         # Same as whatever else
        self.lineEdit1.move(470, 100)          # ... wherever
        #
        # To get text self.lineEdit.text()

        #Input Diameter Value for Pump Address 00
        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setObjectName("frEdit") # Flow-Rate Edit
        self.lineEdit2.setText(" Input Diameter")# Placeholder text
        self.lineEdit2.resize(200, 32)         # Same as whatever else
        self.lineEdit2.move(690, 100)          # ... wherever        
        
        #Input Diameter Value for Pump Address 01
        self.lineEdit3 = QLineEdit(self)
        self.lineEdit3.setObjectName("frEdit") # Flow-Rate Edit
        self.lineEdit3.setText(" Input Diameter")# Placeholder text
        self.lineEdit3.resize(200, 32)         # Same as whatever else
        self.lineEdit3.move(690, 280)          # ... wherever       
        
        #Input Flow Rate Value for Pump Address 01
        self.lineEdit4 = QLineEdit(self)
        self.lineEdit4.setObjectName("frEdit") # Flow-Rate Edit
        self.lineEdit4.setText(" Input flow rate")# Placeholder text
        self.lineEdit4.resize(200, 32)         # Same as whatever else
        self.lineEdit4.move(470, 280)          # ... wherever       
 
        #Input Flow Rate Value for Pump Address 02
        self.lineEdit5 = QLineEdit(self)
        self.lineEdit5.setObjectName("frEdit") # Flow-Rate Edit
        self.lineEdit5.setText(" Input flow rate")# Placeholder text
        self.lineEdit5.resize(200, 32)         # Same as whatever else
        self.lineEdit5.move(470, 460)          # ... wherever     

        #Input Diameter Value for Pump Address 02
        self.lineEdit6 = QLineEdit(self)
        self.lineEdit6.setObjectName("frEdit") # Flow-Rate Edit
        self.lineEdit6.setText(" Input Diameter")# Placeholder text
        self.lineEdit6.resize(200, 32)         # Same as whatever else
        self.lineEdit6.move(690, 460)          # ... wherever 

        self.statusBar()
        self.setGeometry(200, 200, 1000, 800) #(X Window Coor, Y Window Coor, Width Window, Height Window)
        self.setWindowTitle('Syringe Pump Controller')
        
        #Was an area for my logo, or can be used to display an image of diam info
        #label = QLabel(self)
        #pixmap = QPixmap('C:/Users/username/Pictures/example.png')
        #label.setPixmap(pixmap)
        #label.move(50,1)
        #label.resize(120,145)
        #label.setPixmap(pixmap)        
        
        self.show()
     
    def diambuttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba1 = QByteArray
        ba1 = b"MMD " + str(self.lineEdit2.text()).encode('ascii') + b"\r"
        ser.write(ba1)             #b"MMD 22\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()     
    
    def sfrbuttonClicked(self):  
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba = QByteArray
        ba = b"MLH " + str(self.lineEdit1.text()).encode('ascii') + b"\r"
        ser.write(ba)    #b"MLH 2\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()
        
    def ulhbuttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba2 = QByteArray
        ba2 =b"ULH " + str(self.lineEdit1.text()).encode('ascii') + b"\r"
        ser.write(ba2)
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()
        
    def ulmbuttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba3 = QByteArray
        ba3 = b"ULM " + str(self.lineEdit1.text()).encode('ascii') + b"\r"
        ser.write(ba3)
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()
             
    def runbuttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ser.write(b"RUN\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
    def run2buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ser.write(b"01RUN\r")        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
    def stopbuttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ser.write(b"STP\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()
      
    def stop2buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ser.write(b"01STP\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
    def mlh2buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba4 = QByteArray
        ba4 = b"01MLH " + str(self.lineEdit4.text()).encode('ascii') + b"\r"
        ser.write(ba4)    #b"MLH 2\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()

    def diam2buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba5 = QByteArray
        ba5 = b"01MMD " + str(self.lineEdit3.text()).encode('ascii') + b"\r"
        ser.write(ba5)             #b"MMD 22\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()   

    def ulh2buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba6 = QByteArray
        ba6 = b"01ULH " + str(self.lineEdit4.text()).encode('ascii') + b"\r"
        ser.write(ba6)    #b"MLH 2\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()

    def ulm2buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba7 = QByteArray
        ba7 = b"01ULM " + str(self.lineEdit4.text()).encode('ascii') + b"\r"
        ser.write(ba7)    #b"MLH 2\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()
        
    def run3buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ser.write(b"02RUN\r")        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def stop3buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ser.write(b"02STP\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')       

    def mlh3buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba8 = QByteArray
        ba8 = b"02MLH " + str(self.lineEdit5.text()).encode('ascii') + b"\r"
        ser.write(ba8)    #b"MLH 2\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()

    def ulh3buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba9 = QByteArray
        ba9 = b"02ULH " + str(self.lineEdit5.text()).encode('ascii') + b"\r"
        ser.write(ba9)    #b"MLH 2\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()

    def ulm3buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba10 = QByteArray
        ba10 = b"02ULH " + str(self.lineEdit5.text()).encode('ascii') + b"\r"
        ser.write(ba10)    #b"MLH 2\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()

    def diam3buttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ba11 = QByteArray
        ba11 = b"02MMD " + str(self.lineEdit6.text()).encode('ascii') + b"\r"
        ser.write(ba11)             #b"MMD 22\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()   
        
    def stopallbuttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ser.write(b"STP\r")
        ser.write(b"01STP\r")
        ser.write(b"02STP\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()

    def runallbuttonClicked(self):
        ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
        ser.write(b"RUN\r")
        ser.write(b"01RUN\r")
        ser.write(b"02RUN\r")
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        ser.close()

    def getint(self):
        num,ok = QInputDialog.getInt(self, "interger input dialog", "enter value")
        if ok:
            self.le2.setText(str(num))
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure want to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            ser = serial.Serial(port='COM1', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=0.5)
            ser.write(b"STP\r")
            ser.write(b"01STP\r")
            ser.write(b"02STP\r")
            ser.close()
        else:
            event.ignore() 
               
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Pumps()
    sys.exit(app.exec_())
