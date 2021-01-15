mport PySimpleGUI as sg
import serial
import serial.tools.list_ports
import numpy as np
import csv
import matplotlib.pyplot as plt



def init():
    global signal
    signal = {}

    ports = serial.tools.list_ports.comports()
    signal["availablePorts"] = []
    for port in ports:
      signal["availablePorts"].append(port.device)
    signal["BaudRate"] = ['110', '150', '300', '1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200','230400', '460800', '921600']
    signal["months"]=["January","February","March","April","May","June","July","August","September","October","November","December"]

init()



layout = [
            [sg.Frame(layout=[
                [sg.Text("Connection Setting")],
                [   sg.Text('Port', size=(5, 1)),
                    sg.Drop(values=(tuple(signal["availablePorts"])), default_value=signal["availablePorts"][0], auto_size_text=True,key="_ports_"),
                    sg.Text('Baud', size=(5, 1)),
                    sg.Drop(values=(tuple(signal["BaudRate"])), default_value=signal["BaudRate"][13], auto_size_text=True,key="_baudrate_")],
                ],title='Connection Setting',title_color='black')],


            [sg.Frame(layout=[
            [sg.Text("Monthly Sales Report")],
            [sg.Drop(values=(signal["months"]),key="_listbox_", auto_size_text=True,default_value=signal["months"][0]),
             sg.Button("Show Graphic",key="_graphic_")]
             ],title='Monthly Sales Report',title_color='black')]]


window = sg.Window("Sales Report",layout)
while True:
 event, values = window.read()




 def aktarma(a,b,port,baudrate):
    ser = serial.Serial(port,baudrate)
    ser.port =port
    ser.baudrate=baudrate
    ser.timeout = 1


    # data = [["350", "250", "250", "150"],["200","300","400","500"],["400", "100", "200", "200"]]
    data = ["350", "250", "250", "150", "200", "300", "400", "500", "400", "100", "200", "200","200", "300", "400", "500","500", "400", "100", "200"]

    lisst = []


    with open('satis.csv', 'w') as file:
        waiting = csv.writer(file, delimiter=',', quotechar='"')
        waiting.writerows(data)





    with open('satis.csv')as readfile:
        readCSV = csv.reader(readfile)
        for row in readCSV:
            test = np.array(row)
            ser.write(bytes(test))
            lisst.append(ser.readline().decode("utf-32").split(","))

        arr = np.array(lisst)
        veri = arr[a:b]
        for i in veri:
            if max(veri)==veri[0]:
                myexplode = [0.2, 0,0,0]
            if max(veri)==veri[1]:
                myexplode = [0, 0.2, 0, 0]
            if max(veri)==veri[2]:
                myexplode = [0, 0, 0.2, 0]
            if max(veri)==veri[3]:
                myexplode = [0, 0, 0, 0.2]
        mylabels = ["Apple", "Banana", "Grape", "Orange"]
        mycolors = ["red", "yellow", "green", "orange"]
        #myexplode = [c, d, e, f]
        plt.pie(veri,labels=mylabels, colors=mycolors, explode=myexplode, shadow=True)
        plt.legend()
        plt.show()

 def graphic(lst1):

    if lst1 == signal["months"][0]:
        aktarma(0, 4, values["_ports_"], values["_baudrate_"])
    if lst1 == signal["months"][1]:
        aktarma(4,8,values["_ports_"], values["_baudrate_"])
    if lst1 == signal["months"][2]:
       aktarma(8,12,values["_ports_"], values["_baudrate_"])
    if lst1 == signal["months"][3]:
       aktarma(12,16, values["_ports_"], values["_baudrate_"])
    if lst1 == signal["months"][4]:
       aktarma(16,20,values["_ports_"], values["_baudrate_"])

 if event =="_graphic_":
    graphic(values["_listbox_"])

 if event == sg.WIN_CLOSED:
    break

 window.close()
