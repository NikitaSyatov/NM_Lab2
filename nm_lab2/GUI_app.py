#!/bin/sh
#!/bin/bash
#!/bin/env python
#!/usr/bin/env rdmd
# -*- coding: utf-8 -*-
# ./.venv/bin/python
#GUI application

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import sys
import traceback
from resolve import u, method_balance
import numpy as np

# In[]:

df_tmp = pd.DataFrame({
    '    1    ': [],
    '    2    ': [],
    '    3    ': [],
    '    4    ': [],
})

fig, graf = plt.subplots(figsize=(5, 5))
# graf = plt.plot([1, 2, 3, 4], [1, 2, 3, 4])

list_q = ['Тестовая', 'Основная']

frame_output_data = [
    [sg.Output(size=(55, 17), key="-DATA-")],
    [sg.Button("Clear", size=(55, 1))],
]

# In[]:
column1 = [
    [sg.DropDown(list_q, default_value=list_q[0], size=(25, 1), key='-SELECTOR-')],
    [sg.Text("Количество участков разбиений", size=(50, 1))],
    [sg.InputText(default_text="2", size=(30, 1), key='-N-')],
    [sg.Submit(size=(24, 1))],
    [sg.Exit(size=(24, 1))]
]

column_table = [
    [sg.Table(values=df_tmp.values.tolist(), headings=df_tmp.columns.tolist(),
            alternating_row_color='darkblue', key='-TABLE-',
            row_height = 25, vertical_scroll_only=False, size=(200, 100),
            justification='left')],
]

column_graf = [
    [sg.Canvas(key="-CANVAS-")],
]

# In[]:
layout = [
    [sg.Column(column1), sg.VerticalSeparator(), sg.Frame("Данные", frame_output_data, element_justification='right')],
    [sg.HorizontalSeparator()],
    [sg.Frame("Таблица точек", column_table, size=(500, 500), key='-SIZETABLE-'), sg.VerticalSeparator(), sg.Column(column_graf, size=(500, 500), justification='left', key='-SIZEGRAF-')],
]

# In[]:
window = sg.Window('LAB1', layout, finalize=True, resizable=True, grab_anywhere=True)

last_w_size = window.size

canvas_elem = window["-CANVAS-"]
canvas = FigureCanvasTkAgg(fig, master=canvas_elem.Widget)
canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

def update_title(table, headings):
    for cid, text in zip(df_tmp.columns.tolist(), headings):
        table.heading(cid, text=text)

def on_resize(event):
    if (last_w_size != window.size):
        width, height = window.size
        window.Element('-SIZETABLE-').set_size((window.size[0]/2 - 50, window.size[1]))
        window.Element('-SIZEGRAF-').set_size((window.size[0]/2, window.size[1]/1.4))
        window.Element('-CANVAS-').set_size((window.size[0]/2, window.size[1]/1.4))
        canvas_elem.Widget.pack(side="top", fill="both", expand=True)

window.TKroot.bind('<Configure>', on_resize)

while True:                             # The Event Loop
    event, values = window.read()
    window.FindElement('-DATA-').Update('')
    # print(event, values) #debug
    # try:
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        selector = values['-SELECTOR-']

        # df = pd.read_table('output.txt', sep = "\t+", engine='python')

        # table = window.Element("-TABLE-").Widget

        # update_title(table, df.columns.tolist())
        
        # window.Element("-TABLE-").Update(values = df.values.tolist())

        print(selector)

        # list_x = [xi for xi in np.arange(0, 1, 0.0001)]
        x, v = method_balance(2, 1)
        list_u = [u(xi) for xi in x]
        graf = plt.plot(x, list_u, "b-")
        graf = plt.plot(x, v, "r-")

        canvas.draw()
    if event == "Clear":
        fig.clear()
        canvas.draw()
    # except Exception as e:
    #         exc_type, exc_value, exc_traceback = sys.exc_info()

# traceback.print_exception(exc_type, exc_value, exc_traceback)
window.close()