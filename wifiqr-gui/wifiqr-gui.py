from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QVBoxLayout, QGridLayout
import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import QRect,QSize
import os
import wifi_qrcode_created
import wifi_qrcode_gener
import re
class MainWindow(QDialog):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()

        self.title = "wifiqr-gui"
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = "icon.png"
        self.InitWindow()

    def InitWindow(self):
        
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
    
        self.show()
        

    def CreateLayout(self):
        self.groupBox = QGroupBox("Select!")
        gridLayout = QGridLayout()

        self.button = QPushButton("Create QR", self)
        # self.button.setIcon(QtGui.QIcon("icon.png"))
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setMinimumHeight(40)
        gridLayout.addWidget(self.button, 0,0)

        self.button1 = QPushButton("Generate QR", self)
        # self.button1.setIcon(QtGui.QIcon("icon.png"))
        self.button1.setIconSize(QtCore.QSize(40, 40))
        self.button1.setMinimumHeight(40)
        gridLayout.addWidget(self.button1, 1,0)
        self.button1.clicked.connect(self.qrgen_switch) 

        self.button2 = QPushButton("Scan QR", self)
        # self.button2.setIcon(QtGui.QIcon("icon.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setMinimumHeight(40)
        gridLayout.addWidget(self.button2, 2,0)

        self.groupBox.setLayout(gridLayout)

    def qrgen_switch(self):
        self.switch_window.emit()

class GeneratorWindow(QDialog):
    import re
    switch_window = QtCore.pyqtSignal()
    os.system("rm /tmp/key.png")
    # os.system("rm /tmp/wifilist.txt")
    # os.system("rm /tmp/wifi.txt")
    def __init__(self):
        super().__init__()
        self.title = "wifiqr-gui"
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = "icon.png"
        self.ssidgen()
        self.xdgop = "xdg-open '/tmp/key.png'"
        ssidraw = self.button_pushed(self)
        pskraw = wifi_qrcode_gener.pskgen()
        ssid = ssidraw[5:]
        hidden = False
        autheraw = wifi_qrcode_gener.authtype().upper()
        authentication_type = autheraw[9:12]
        password = pskraw[4:]
        code = wifi_qrcode_created.wifi_qrcode(ssid, hidden, authentication_type, password)
        code.save('/tmp/key.png')
        self.InitWindowGenerate()

    def InitWindowGenerate(self):
        os.system("rm /tmp/key.png")
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.ssidgen()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
    
        self.show()

    def ssidgen(self):
    # def ssidgen():
        os.system("ls -1 /etc/NetworkManager/system-connections/ > /tmp/wifilist.txt")
        with open("/tmp/wifilist.txt", 'r') as file_handle:
        # read file content into list
            lines = file_handle.readlines()
    # print list content
        self.groupBox = QGroupBox("Select!")
        gridLayout = QGridLayout()
        for btn_name in lines:
            self.button = QPushButton(btn_name[0:-14], self)
            # text = self.button.text()
            # self.button.setIcon(QtGui.QIcon("icon.png"))
            self.button.setIconSize(QtCore.QSize(40, 40))
            self.button.setMinimumHeight(40)
            gridLayout.addWidget(self.button)
            text = self.button.text()
            self.button.clicked.connect(lambda ch, text=text :self.button_pushed(text))
          
        self.groupBox.setLayout(gridLayout)
        file_handle.close()
    def button_pushed(self, text):
        
        print(text)
        os.system(self.xdgop)
        # inputnum = int(input("Enter Number of Name:"))
        cont = ".nmconnection"
        catt = str(text)
        # print(catt)
        os.system(f" sudo cat /etc/NetworkManager/system-connections/{str(catt+cont)} > /tmp/wifi.txt",)
        
        f = open("/tmp/wifi.txt",'r')
        with f as open_file:
            data = open_file.read()
            reg = []
            reg = self.re.findall(r'ssid=.*',data)
            for i in reg:
                #print (i)
                return i
            return button_pushed()
        
    def clickme(self):
        print("worked")
class Controller:

    def __init__(self):
        pass

    def show_main(self):
        self.main = MainWindow()
        self.main.switch_window.connect(self.show_generate)
        self.main.show()
    def show_generate(self):
        self.generate = GeneratorWindow()
        self.show_generate.switch_window.connect(self.show_generate)
        self.show_generate()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(App.exec())


