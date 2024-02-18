# User Input Window - A simple user input window program
# Copyright (c) 2022 Ercan Ersoy
# This file licensed under MIT License.

import PySimpleGUI as sg

sg.theme("SystemDefaultForReal")

layout = [[sg.Text("Input:"), sg.In(size=(50, 1), key="INPUT"), sg.Button("OK")]]

window = sg.Window("User Input Window", layout, element_justification="c",
                   size=(500, 100), finalize=True)

while True:
    event, values = window.read()

    if event == "OK":
        print(values["INPUT"])
        break

    if event == sg.WIN_CLOSED:
        break

window.close()
