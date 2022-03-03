#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:52:46 2022

@author: shaurjyamandal
"""


from tkinter import *
from PIL import ImageTk, Image
import random

root= Tk()
root.geometry("600x400")
root.title('Image Focus test')
root.iconbitmap('/Users/shaurjyamandal/Downloads')

print("Choose your favorite animal \n 1) dog \n 2)cat \n 3)cow \n 4)sheep \n 5)tiger \n 6)goat")
ans=int(input())
print(ans)
global our_images, count
count = 0
global correct
global wrong
correct=0
wrong=0
a = Image.open("animals/dog.png").resize((600,400))
b = Image.open("animals/cat.png").resize((600,400))
c = Image.open("animals/cow.png").resize((600,400))
d = Image.open("animals/sheep.png").resize((600,400))
e = Image.open("animals/tiger.png").resize((600,400))
f = Image.open("animals/goat.png").resize((600,400))
#a = a.resize(1000,800)
our_images = [
       ImageTk.PhotoImage(a),
       ImageTk.PhotoImage(b),
       ImageTk.PhotoImage(c),
       ImageTk.PhotoImage(d),
       ImageTk.PhotoImage(e),
       ImageTk.PhotoImage(f)
       ]


my_canvas = Canvas (root, width=1000, height=800, highlightthickness=0)
my_canvas.pack()

my_canvas.create_image(0,0, image= our_images[0],anchor= 'nw')

#button1 = Button(root, text = "Click me", anchor = 'nw')
#button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
#button1_window = my_canvas.create_window(100, 200, anchor='nw', window=button1)

def got_clicked():
  print("I got clicked!")
  
def next():
    global count
    count=random.randint(0,5)
    my_canvas.create_image(0,0, image= our_images[count],anchor= 'nw')
    '''
    global count
    if count ==2:
        my_canvas.create_image(0,0, image= our_images[0],anchor= 'nw')
        count=0
    else:
        my_canvas.create_image(0,0, image= our_images[count],anchor= 'nw')
        count +=1
     '''   
    print ("hi")
    root.after(1000, next)
    
def answer():
   global correct,wrong,count
   if(count==ans-1):
       correct=correct+1
   else:
       wrong=wrong+1
   count=random.randint(0,5)
   my_canvas.create_image(0,0, image= our_images[count],anchor= 'nw')
   print("hello")
   print (wrong," ",correct)
    
button1 = Button(root, text = "Click me", anchor = 'nw', command=answer)
button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button1_window = my_canvas.create_window(100, 200, anchor='nw', window=button1)
    
next()
#print (wrong," ",correct)
mainloop()