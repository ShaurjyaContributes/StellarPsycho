#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 12:34:08 2022

@author: shaurjyamandal
"""
from tkinter import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

import xlwt
from xlwt import Workbook

wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine, PageTen):
        #for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
     

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):


        
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 0, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you been upset because of something that happened unexpectedly?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var0=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var0, value=0, command=lambda: clicked(var0.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var0, value=1, command=lambda: clicked(var0.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var0, value=2, command=lambda: clicked(var0.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var0, value=3, command=lambda: clicked(var0.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var0, value=4, command=lambda: clicked(var0.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("StartPage"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageTwo"))
        button2.place(x=875, y=700)
        
    
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 1, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you felt that you were unable to control the important things in your life?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var1=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var1, value=0, command=lambda: clicked(var1.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var1, value=1, command=lambda: clicked(var1.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var1, value=2, command=lambda: clicked(var1.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var1, value=3, command=lambda: clicked(var1.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var1, value=4, command=lambda: clicked(var1.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("PageOne"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageThree"))
        button2.place(x=875, y=700)
        
class PageThree(tk.Frame):
    
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 2, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you felt nervous and stressed?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var2=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var2, value=0, command=lambda: clicked(var2.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var2, value=1, command=lambda: clicked(var2.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var2, value=2, command=lambda: clicked(var2.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var2, value=3, command=lambda: clicked(var2.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var2, value=4, command=lambda: clicked(var2.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("PageTwo"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageFour"))
        button2.place(x=875, y=700)
        
class PageFour(tk.Frame):
    
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 3, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you felt confident about your ability to handle your personal problems?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var3=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var3, value=4, command=lambda: clicked(var3.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var3, value=3, command=lambda: clicked(var3.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var3, value=2, command=lambda: clicked(var3.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var3, value=1, command=lambda: clicked(var3.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var3, value=0, command=lambda: clicked(var3.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("PageThree"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageFive"))
        button2.place(x=875, y=700)
        
class PageFive(tk.Frame):
    
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 4, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you felt that things were going your way?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var4=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var4, value=4, command=lambda: clicked(var4.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var4, value=3, command=lambda: clicked(var4.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var4, value=2, command=lambda: clicked(var4.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var4, value=1, command=lambda: clicked(var4.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var4, value=0, command=lambda: clicked(var4.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("PageFour"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageSix"))
        button2.place(x=875, y=700)
        
class PageSix(tk.Frame):
    
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 5, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you found that you could not cope with all the things that you had to do?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var5=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var5, value=0, command=lambda: clicked(var5.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var5, value=1, command=lambda: clicked(var5.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var5, value=2, command=lambda: clicked(var5.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var5, value=3, command=lambda: clicked(var5.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var5, value=4, command=lambda: clicked(var5.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("PageFive"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageSeven"))
        button2.place(x=875, y=700)
        
class PageSeven(tk.Frame):
    
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 6, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you been able to control irritations in your life?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var6=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var6, value=4, command=lambda: clicked(var6.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var6, value=3, command=lambda: clicked(var6.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var6, value=2, command=lambda: clicked(var6.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var6, value=1, command=lambda: clicked(var6.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var6, value=0, command=lambda: clicked(var6.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("PageSix"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageEight"))
        button2.place(x=875, y=700)
        
class PageEight(tk.Frame):
    
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 7, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you felt that you were on top of things?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var7=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var7, value=4, command=lambda: clicked(var7.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var7, value=3, command=lambda: clicked(var7.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var7, value=2, command=lambda: clicked(var7.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var7, value=1, command=lambda: clicked(var7.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var7, value=0, command=lambda: clicked(var7.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("PageSeven"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageNine"))
        button2.place(x=875, y=700)
        
class PageNine(tk.Frame):
    
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 8, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you been angered because of things that happened that were outside of your control?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var8=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var8, value=0, command=lambda: clicked(var8.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var8, value=1, command=lambda: clicked(var8.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var8, value=2, command=lambda: clicked(var8.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var8, value=3, command=lambda: clicked(var8.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var8, value=4, command=lambda: clicked(var8.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("PageEight"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageTen"))
        button2.place(x=875, y=700)
        
class PageTen(tk.Frame):
    
    def __init__(self, parent, controller):
        
        def clicked(value):
            sheet1.write(0, 9, value)
            #wb.save('example.xls')
            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        #Radiobutton(root, text="Type II",  variable = radiobutton_variable, value = 1)
        var9=IntVar()
        c1 = tk.Radiobutton(self,text="Never",variable=var9, value=0, command=lambda: clicked(var9.get()))
        c1.place(x=600,y=200)
        c2 = tk.Radiobutton(self,text="Almost Never",variable=var9, value=1, command=lambda: clicked(var9.get()))
        c2.place(x=600,y=300)
        c3 = tk.Radiobutton(self,text="Sometimes",variable=var9, value=2, command=lambda: clicked(var9.get()))
        c3.place(x=600,y=400)
        c4 = tk.Radiobutton(self,text="Fairly Often",variable=var9, value=3, command=lambda: clicked(var9.get()))
        c4.place(x=600,y=500)
        c5 = tk.Radiobutton(self,text="Very Often",variable=var9, value=4, command=lambda: clicked(var9.get()))
        c5.place(x=600,y=600)
        button1 = tk.Button(self, text="Previous Question",
                           command=lambda: controller.show_frame("PageNine"))
        button1.place(x=725, y=700)
        button2 = tk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame("PageOne"))
        button2.place(x=875, y=700)

'''       
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
'''

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    wb.save('example.xls')
    #print(t1)
    
    
    
    
    
    