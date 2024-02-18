# Simple Window - A simple window program
# Copyright (c) 2022 Ercan Ersoy
# This file licensed under MIT License.

import PySimpleGUI as sg

sg.theme("SystemDefaultForReal")

layout = [[sg.Text("Example Message")]]

window = sg.Window("Simple Window", layout, element_justification="c",
                   size=(300, 100), finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
