from PyQt5 import QtWidgets , QtCore
from patient import Ui_MainWindow
import sys
import random
from bluezero import adapter
import logging
import bluetooth as bt 
from bluepy.btle import Scanner, DefaultDelegate
from bluepy import *
import asyncio
from bleak import discover, BleakClient


class patientSignal(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(patientSignal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connectbtn.clicked.connect(self.connectbtn_clicked)
        #self.ui.sendbtn.clicked.connect(self.sendbtn_clicked)
        self.ui.sendbtn.clicked.connect(self.tryfun)
        DefaultDelegate.__init__(self)
        self.devices = []

    def connectbtn_clicked(self):
        target_name = "MyESP32" 
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
            port = [_ for _ in bt.find_service(address=address) if 'RFCOMM' in _['protocol']][0]['port']
            client_socket=bt.BluetoothSocket( bt.RFCOMM )
            client_socket.connect((address, port))
            self.ui.statuslbl.setText("connected")
            client_socket.send(self.generateSignal())
            print ("Sent")
            client_socket.close()
            print("closed")
        else:
            print ("could not find target bluetooth device nearby")

    def sendbtn_clicked(self):
        dongles = adapter.list_adapters()

        dongle = adapter.Adapter(dongles[0])
        if(not dongle.discoverable):
            dongle.discoverable = True
        if not dongle.powered:
            dongle.powered = True

        print("scaning . . . ")
        scanner = Scanner().withDelegate(DefaultDelegate.__init__(self))
        devices = scanner.scan(10.0)
        for dev in devices:
            print(dev.addr)
            if (dev.addr ==  "a4:cf:12:0a:7e:c2"):
                connection = btle.Peripheral(dev.addr,dev.addrType)
                #connection.connect(dev.addr,dev.addrType)
                print("connected")
                connection.pair()
                print("paired")
        print("failed")
            #print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
            #for (adtype, desc, value) in dev.getScanData():
            #    print ("  %s = %s" % (desc, value))
        
    #async def run(self):
    #    devices = await discover()
    #    for d in devices:
    #        print(d)


    async def scan(self):
        dev = await discover()
        for i in range(0,len(dev)):
            print("["+str(i)+"]"+str(dev[i]))
            self.devices.append(dev[i])

    async def connect(self, address, loop):
        async with BleakClient(address, loop=loop) as client:
            services = await client.get_services()
            for ser in services:
                print(ser.uuid)

    async def run(self, address, loop):
        async with BleakClient(address, loop=loop) as client:
            model_number = await client.read_gatt_char(MODEL_NBR_UUID)
            print("Model Number: {0}".format("".join(map(chr, model_number))))

    def tryfun(self):
        #address = "a4:cf:12:0a:7e:c2"
        address = "77-92-9A-D4-D5-F5"
        #MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"

        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(self.run())

        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(self.run(address, loop))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.scan())
        index = input('please select device from 0 to '+str(len(self.devices))+":")
        index = int(index)
        loop.run_until_complete(self.connect(self.devices[index].address, loop))
        print("DONE")
        

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)

    def generateSignal (self):
        signal = random.randint(0,100)
        return signal



        



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = patientSignal()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()