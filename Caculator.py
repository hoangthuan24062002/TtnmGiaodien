import tkinter as tk

# Function to handle button clicks
def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Create a tkinter window
root = tk.Tk()
root.title("Virtual Calculator")
root.geometry("400x500")

# Create an input field
screen = tk.StringVar()
input_field = tk.Entry(root, textvar=screen, font="lucida 20 bold")
input_field.pack(fill=tk.X, padx=10, pady=10, ipadx=8, ipady=8)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row, col = 1, 0
for button_text in buttons:
    button = tk.Button(
        button_frame,
        text=button_text,
        font="lucida 15 bold",
        padx=20,
        pady=20,
        relief=tk.RIDGE,
    )
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

    # Bind button click event
    button.bind("<Button-1>", button_click)

# Start the tkinter main loop
root.mainloop()
