#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:19:07 2022

@author: shaurjyamandal
"""

from tkinter import *
import serial
import numpy
import time
window= Tk()
#window shape
window.geometry("600x400")
#window title
window.title('Synchronization Test')
#location
window.iconbitmap('/Users/shaurjyamandal/Downloads')  
v1=[]
cond = False
i=0
j=0
k=0
ser = serial.Serial(port='/dev/cu.usbserial-1410', baudrate=9600, timeout=1)
#ser.reset_input_buffer()
def save_data():
    global cond
    global k
    k=k+1
    if (cond == True):
        global i
        i=i+1
        if(ser.readline()!= None):
            global j
            j=j+1
            v = ser.readline().decode('ascii')
            v1.append(str(v))
            print(str(v))
            
    '''
    if (cond == True and ser.readline()!= None):
        v = ser.readline().decode('ascii')
        v1.append(str(v))
        print(str(v))
    '''
    #if (cond==True)
    window.after(1,save_data)
    
label = Label(window, text="Data record testing", font=("Helvetica",18)).pack()

def start():
    global cond
    cond=True
    #global i
    #i = 1
    save_data()
    
    #ser = serial.Serial(port='/dev/cu.usbserial-1410', baudrate=9600, timeout=1)
    ser.open()
    #ser.reset_input_buffer()
    
def stop():
    global cond
    cond = False
    #global i
    #i = 0
    ser.close()
    #numpy.savetxt('Output1.txt', v1, fmt='%s')
'''
#ser = serial.Serial(port='/dev/cu.usbserial-1410', baudrate=9600, timeout=1)
def start():
    ser = serial.Serial(port='/dev/cu.usbserial-1410', baudrate=9600, timeout=1)
    while True:
        v = ser.readline().decode('ascii')
        v1.append(str(v))
        print(str(v))
        time.sleep(0.001)
        
def stop():
    ser.close()
    
def save_data():
    numpy.savetxt('Output.txt', v1, fmt='%s')
 '''   
button1 = Button(window, text="Start", command=lambda: start()).place(x=600,y=200)

button2 = Button(window, text="Stop", command=lambda: stop()).place(x=700,y=200)

#window.after(1,save_data)
window.mainloop()
print(i,"  ",j,"  ",k)
numpy.savetxt('Output1.txt', v1, fmt='%s')
