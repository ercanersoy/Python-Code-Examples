# User Input Window - A simple user input window program
# Copyright (c) 2022 Ercan Ersoy
# This file licensed under MIT License.
# Write this code using GitHub Copilot.

import tkinter as tk

def on_button_click():
    print(input_entry.get())
    window.destroy()

window = tk.Tk()
window.title("User Input Window")
window.geometry("400x100")

frame = tk.Frame(window)
frame.pack(anchor="center")

input_label = tk.Label(frame, text="Input")
input_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

input_entry = tk.Entry(frame, width=50)
input_entry.grid(row=1, column=0, padx=5, pady=5)

ok_button = tk.Button(frame, text="OK", command=on_button_click)
ok_button.grid(row=1, column=1, sticky="e", padx=5, pady=5)

window.mainloop()
