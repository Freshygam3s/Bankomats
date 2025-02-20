import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import json

#json
with open('Bankomats\kartes_dati.json', 'r') as file:
    data = json.load(file)
print(data)
    
#window
window = tk.Tk()
window.title("Bank")
window.geometry("1500x800")
window.configure(bg="purple")

#variables
PIN_var = tk.StringVar()
#frames
PIN_frame = tk.Frame(window, bg="purple") 
lang_frame = tk.Frame(window)
button_frame = tk.Frame(window)
button_frame_1 = tk.Frame(window)
button_frame_2 = tk.Frame(window)
button_frame_3 = tk.Frame(window)


#widgets
pin_text = tk.Label(window, text = "Put in your card:", bg="purple", font="Arial 45 bold")
PIN_label = tk.Label(PIN_frame, text = "PIN:", bg="purple", font="Arial 35 bold")
PIN_entry = tk.Entry(PIN_frame, show="*", font="Arial 15", textvariable=PIN_var)

#functions
def enter_func():
    PIN_val = PIN_var.get()
    print(PIN_val)

#flags
image = Image.open('/images/eng.png')
image = image.resize((50, 30), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

image2 = Image.open('/images/lv.png')
image2 = image2.resize((50, 30), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open('/images/rus.jpeg')
image3 = image3.resize((50, 30), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)


#buttons
eng_btn = tk.Button(lang_frame, text="ENG", image=photo, compound="center", bg="black", font="bold")
eng_btn.pack(side="left")
lv_btn = tk.Button(lang_frame, text="LV", image=photo2, compound="center", bg="black", font="bold")
lv_btn.pack(side="left")
rus_btn = tk.Button(lang_frame, text="RUS", image=photo3, compound="center", bg="black", font="bold")
rus_btn.pack(side="left")
numb_1 = tk.Button(button_frame, text="1",height= 5, width=10)
numb_1.pack(side="left")
numb_2 = tk.Button(button_frame, text="2",height= 5, width=10)
numb_2.pack(side="left")
numb_3 = tk.Button(button_frame, text="3",height= 5, width=10)
numb_3.pack(side="left")

numb_4 = tk.Button(button_frame_1, text="4",height= 5, width=10)
numb_4.pack(side="left")
numb_5 = tk.Button(button_frame_1, text="5",height= 5, width=10)
numb_5.pack(side="left")
numb_6 = tk.Button(button_frame_1, text="6",height= 5, width=10)
numb_6.pack(side="left")

numb_7 = tk.Button(button_frame_2, text="7",height= 5, width=10)
numb_7.pack(side="left")
numb_8 = tk.Button(button_frame_2, text="8",height= 5, width=10)
numb_8.pack(side="left")
numb_9 = tk.Button(button_frame_2, text="9",height= 5, width=10)
numb_9.pack(side="left")

delete = tk.Button(button_frame_3, text="DEL",height= 5, width=10)
delete.pack(side="left")
numb_0 = tk.Button(button_frame_3, text="0",height= 5, width=10)
numb_0.pack(side="left")
Enter = tk.Button(button_frame_3, text="Enter",height= 5, width=10, command= enter_func)
Enter.pack(side="left")

eng_btn.image = photo
# pack
lang_frame.pack()
pin_text.pack()
PIN_label.pack(side="left")
PIN_entry.pack(side="left")
PIN_frame.pack()
button_frame.pack()
button_frame_1.pack()
button_frame_2.pack()
button_frame_3.pack()


#mainloop
window.mainloop()
