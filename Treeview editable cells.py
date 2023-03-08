import tkinter as tk
from tkinter import ttk


class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.bind("<Double-1>", self.on_double_click)

    def on_double_click(self, event):
        print("double clicked")


if __name__ == "__main__":

    root = tk.Tk()

    column_names = ("vehicle_name", "year", "colour")

    treeview_vehicles = TreeviewEdit(root, columns=column_names)
    treeview_vehicles.heading("#0", text="Vehicle Type")
    treeview_vehicles.heading("vehicle_name", text="Vehicle Name")
    treeview_vehicles.heading("year", text="Year")
    treeview_vehicles.heading("colour", text="Colour")

    sedan_row = treeview_vehicles.insert(parent="", index=tk.END, text="Sedan") # dodawanie parenta

    treeview_vehicles.insert(parent=sedan_row, index=tk.END, values=("Nissan Versa", "2010", "Silver"))
    treeview_vehicles.insert(parent=sedan_row, index=tk.END, values=("Toyota Camry", "2012", "Blue"))

    treeview_vehicles.pack(fill=tk.BOTH, expand=True)

    root.mainloop()