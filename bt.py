from PyQt5 import QtWidgets , QtCore
from patient import Ui_MainWindow
import sys
import numpy as np
import bluetooth as bt 

class patientSignal(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(patientSignal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectbtn.clicked.connect(self.connectbtn_clicked)
        #self.ui.sendbtn.clicked.connect(self.sendbtn_clicked)

    def connectbtn_clicked(self):
        target_name = "Peter A6" 
        address = 0 
        print ("performing inquiry...")
        nearby_devices = bt.discover_devices(lookup_names = True)
        print ("found %d devices" % len(nearby_devices))
        for addr, name in nearby_devices:
            #print (" %s - %s" % (addr, name))
            print (name)
            if target_name == name:
                address = addr
        
        if (address != 0):
            print ("found target bluetooth device with address ", address)
            port = 3
            client_socket=bt.BluetoothSocket( bt.RFCOMM )
            client_socket.connect((address, port))
            self.ui.statuslbl.setText("connected")
            client_socket.send("Hello World")
            print ("Finished")
            client_socket.close()
        else:
            print ("could not find target bluetooth device nearby")


    #def sendbtn_clicked(self):



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = patientSignal()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()