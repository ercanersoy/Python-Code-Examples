# Simple Window - A simple window program
# Copyright (c) 2022 Ercan Ersoy
# This file licensed under MIT License.
# Write this code using GitHub Copilot.

import tkinter as tk

window = tk.Tk()
window.title("Simple Window")
window.geometry("300x100")

label = tk.Label(window, text="Example Message")
label.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()
