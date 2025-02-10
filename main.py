import tkinter as tk

#window
window = tk.Tk()
window.title("Bank")
window.geometry("1500x800")
window.configure(bg="purple")



#frames
lang_frame = tk.Frame(window)
button_frame = tk.Frame(window)
button_frame_1 = tk.Frame(window)
button_frame_2 = tk.Frame(window)
button_frame_3 = tk.Frame(window)

#buttons
eng_btn = tk.Button(lang_frame, text="Eng")
eng_btn.pack(side="left")
lv_btn = tk.Button(lang_frame, text="Lv")
lv_btn.pack(side="left")
rus_btn = tk.Button(lang_frame, text="Rus")
rus_btn.pack(side="left")
numb_1 = tk.Button(button_frame, text="1")
numb_1.pack(side="left")
numb_2 = tk.Button(button_frame, text="2")
numb_2.pack(side="left")
numb_3 = tk.Button(button_frame, text="3")
numb_3.pack(side="left")

numb_4 = tk.Button(button_frame_1, text="4")
numb_4.pack(side="left")
numb_5 = tk.Button(button_frame_1, text="5")
numb_5.pack(side="left")
numb_6 = tk.Button(button_frame_1, text="6")
numb_6.pack(side="left")

numb_7 = tk.Button(button_frame_2, text="7")
numb_7.pack(side="left")
numb_8 = tk.Button(button_frame_2, text="8")
numb_8.pack(side="left")
numb_9 = tk.Button(button_frame_2, text="9")
numb_9.pack(side="left")

delete = tk.Button(button_frame_3, text="DEL")
delete.pack(side="left")
numb_0 = tk.Button(button_frame_3, text="0")
numb_0.pack(side="left")
Enter = tk.Button(button_frame_3, text="Enter")
Enter.pack(side="left")

# pack
lang_frame.pack()
pin_text = tk.Label(window, text = "Put in your card:", bg="purple", font="Arial 45 bold")
pin_text.pack()
button_frame.pack()
button_frame_1.pack()
button_frame_2.pack()
button_frame_3.pack()


#mainloop
window.mainloop()
