import serial
import serial.tools.list_ports
import numpy as np
import gui



def init():

   ports = serial.tools.list_ports.comports()
   gui.signal["avaliablePorts"] = []
   for port in ports:
      gui.signal["avaliablePorts"].append(port)
