# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()
root.geometry("1370x850")
root.config(bg = 'White')
# Adding widgets to the root window
heading = Label(root, text = 'Welcome to Neurostellar Psychometry Test', font =(
'Times New Roman', 25))
heading.pack(side = TOP, pady = 10)
# Creating a photoimage object to use image
photo = PhotoImage(file = r"E:\Aditya\Psychometry\download.png")
#photo = photo.subsample(2)


def MIST_TEST():
    root.destroy()
    import MIST
def PSS_TEST():
    root.destroy()
    import PSS
def FOCUS_TEST():
    root.destroy()
    import FOCUS
# here, image option is used to
# set image on button
Button(root, text = 'Click Me !', image = photo).pack(side = TOP)
b1 = Button(root, text = 'MIST TEST',command = MIST_TEST).place(x = 650,y = 300)
b2 = Button(root, text = 'PSS QUESTIONARRE',command = PSS_TEST).place(x = 450,y = 300)
b3 = Button(root, text = 'FOCUS TEST',command = FOCUS_TEST).place(x = 800,y = 300)

mainloop()






































