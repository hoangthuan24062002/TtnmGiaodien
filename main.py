# import Tkinter module
from tkinter import *
from tkinter import messagebox

# Tạo cửa sổ chính của ứng dụng GUI
top = Tk()
# Gọi vòng lặp sự kiện chính để các hành động có thể diễn ra trên màn hình máy tính của người dùng
top.geometry("200x100")


def clickRedButton():
    messagebox.showinfo("Hello", "Red Button clicked")


def clickBlueButton():
    messagebox.showinfo("Hello", "Blue Button clicked")

def clickGreenButton():
    messagebox.showinfo("Hello", "Green Button clicked")

def clickYellowButton():
    messagebox.showinfo("Hello", "Yellow Button clicked")

b1 = Button(top, text="Red", command=clickRedButton, activeforeground="red", activebackground="pink", pady=10)
b2 = Button(top, text="Blue", command=clickBlueButton, activeforeground="blue", activebackground="pink", pady=10)
b3 = Button(top, text="Green", command=clickGreenButton, activeforeground="green", activebackground="pink", pady=10)
b4 = Button(top, text="Yellow", command=clickYellowButton, activeforeground="yellow", activebackground="pink", pady=10)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)
top.mainloop()