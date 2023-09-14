import tkinter as tk

def button_click(number):
    current = entry.get()
    if number == 'Hoang Van Thuan':
        entry.delete(0, tk.END)
        entry.insert(0, '0')
    else:
        entry.delete(0, tk.END)
        entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Lỗi")

# Tạo cửa sổ giao diện đồ họa
window = tk.Tk()
window.title("Máy tính cầm tay")
window.geometry("400x600")  # Đặt kích thước cửa sổ

# Tạo ô nhập liệu
entry = tk.Entry(window, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Tạo các nút số và phép toán
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    ('Hoang Van Thuan', 4),  # Change to a tuple with the button text and columnspan
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    if isinstance(button_text, tuple):  # If it's a tuple of buttons
        tk.Button(
            window, text=button_text[0], padx=20, pady=20, font=('Arial', 15),
            command=lambda b=button_text[0]: button_click(b) if b != '=' else calculate()
        ).grid(row=row_val, column=col_val, columnspan=button_text[1], padx=5, pady=5)
    else:
        tk.Button(
            window, text=button_text, padx=20, pady=20, font=('Arial', 15),
            command=lambda   b=button_text: button_click(b) if b != '=' else calculate()
        ).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += button_text[1] if isinstance(button_text, tuple) else 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Nút xóa
tk.Button(
    window, text='C', bg="red", activeforeground="green", activebackground="pink", padx=20, pady=20, font=('Arial', 15),
    command=clear).grid(row=row_val, column=col_val, padx=5, pady=5)

# Bắt đầu vòng lặp chạy ứng dụng
window.mainloop()
