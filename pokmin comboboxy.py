import tkinter as tk
from tkinter import ttk

root = tk.Tk()

combo1 = ttk.Combobox(root, values=['Option 1', 'Option 2', 'Option 3'])
combo1.pack()

combo2 = ttk.Combobox(root, state='disabled')
combo2.pack()

def enable_combo2(event):
    combo2['state'] = 'readonly'
    combo2['values'] = ['Suboption 1', 'Suboption 2', 'Suboption 3']

combo1.bind('<<ComboboxSelected>>', enable_combo2)

root.mainloop()