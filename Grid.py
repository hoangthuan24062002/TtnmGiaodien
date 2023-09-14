import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)

# Configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Username label and entry
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# Password label and entry
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root, show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# Login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

# Start the main event loop
root.mainloop()
