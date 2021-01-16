import PySimpleGUI as sg
import serial
import serial.tools.list_ports
import numpy as np
import csv
import matplotlib.pyplot as plt

mnt=["January","February","March","April","May","June","July","August","September","October","November","December"]

layout=[[sg.Text("Analysis")],
    [sg.Text('buying amount'),
     sg.InputText(key="_number1_",size=(10,10)),
     sg.Text('sales amount'), sg.InputText(key="_number2_",size=(10,10)),
     sg.Drop(values=(mnt),key="_listbox_", auto_size_text=True,default_value=mnt[0]),
     sg.Button("Save information",key="_button_"),
     sg.Button("comparison graphic",enable_events=True,key="_graphic_"),
     sg.Button("Safe Exit",key="_Exit_")]]



window = sg.Window("Sales Report",layout)
stslist = []
alslist = []
months = [""]
gainlist = ["0"]



while True:
 event, values = window.read()

 if event =="_button_":


      if values["_number1_"] == "" or values["_number2_"] == "":
          sg.Popup("! Login information is missing. Try again")
      else:
          if values["_number1_"].isalpha() or values["_number2_"].isalpha():
              sg.Popup("! Wrong entry.Please enter number")
          else:
              data1 = ""
              for i in (values["_number1_"]):
                  data1 += i
              stslist.append(data1)
              data2 = ""
              for a in (values["_number2_"]):
                  data2 += a
              alslist.append(data2)
              month = ""
              for m in (values["_listbox_"]):
                  month += m
              months.append(month)

              gainValues = ""

              gain = round((float(values["_number2_"]) - float(values["_number1_"])) * 100) / (
                  float(values["_number1_"]))
              for k in str(gain):
                  gainValues += k
              gainlist.append(gainValues)


 def graphic():

   x = np.array(months)
   y = np.array(gainlist)
   plt.bar(x, y,width = 0.3)
   plt.show()




 if event== "_graphic_":
     if values["_number1_"] == "" or values["_number2_"] == "":
         sg.Popup("!please save the information first ")
     else:
         graphic()
         break
 if event == sg.WIN_CLOSED:
     window.close()


 if event=="_Exit_":
    window.close()
    break
