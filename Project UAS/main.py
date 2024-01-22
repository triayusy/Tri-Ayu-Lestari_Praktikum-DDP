from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="darkly")

#root = Tk()
root.title("TTK Boostrap!")
root.iconbitmap('images/logoparkir.png')
root.geometry('500x350')

# Create a Function for the Button
counter = 0
def changer():
    counter += 1
    if counter % 2 == 0:
        my_label.config(text="")
    else:
        my_label.config(text="")


# Colors:
# Default, primary, secondary, succuess, info, warning, danger
# Light, dark

# Create a Label
my_label = tb.Label(text="Program Karcis Parkir", font=("Helvetica", 10), 
    bootstyle="default")
my_label.pack(pady=50)

# Create a Button
my_button = tb.Button(text="Submit", 
                      bootstyle="succes, outline", command=changer)