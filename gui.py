import PySimpleGUI as sg
import serial
import serial.tools.list_ports
import numpy as np
import conn


def init():
    global signal

    signal = {}
    conn.init()
    signal["BaudRate"] = ['110', '150', '300', '1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200','230400', '460800', '921600']
    signal["SerialConnection"] = None
    signal["SerialConnectionStatus"] = ["Connect", "green"]

init()

layout = [
            [sg.Frame(layout=[
                [sg.Text('Connection Setting')],
                [   sg.Text('Port', size=(5, 1)),
                    sg.Drop(values=(tuple(signal["avaliablePorts"])), default_value=signal["avaliablePorts"][0], auto_size_text=True), # -> values[1],  default=ttyUSB0, first terminal
                    sg.Text('Baud', size=(5, 1)),
                    sg.Drop(values=(tuple(signal["BaudRate"])), default_value=signal["BaudRate"][13], auto_size_text=True)]],title='Connection Setting',title_color='black', relief=sg.RELIEF_SUNKEN, tooltip='Use these to get ADC values')]]


