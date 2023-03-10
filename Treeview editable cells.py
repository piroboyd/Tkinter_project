import tkinter as tk
from tkinter import ttk


class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.bind("<Double-1>", self.on_double_click)

    def on_double_click(self, event):

        # Identify the region that was double-clicked
        region_clicked = self.identify_region(event.x, event.y)

        # If the clicked region is not a cell or tree, return None.
        # We are only interested in cell and tree.
        if region_clicked not in ("cell", "tree"):
            return

        # Which item was double-clicked
        column = self.identify_column(event.x)
        column_index = int(column[1:]) - 1

        # For example: 001
        selected_iid = self.focus()

        # This will contain both text and values from the given item iid
        selected_values = self.item(selected_iid)

        if column == "#0":
            selected_text = selected_values.get("text")
        else:
            selected_text = selected_values.get("values")[column_index]

        column_box = self.bbox(selected_iid, column)

        entry_edit = ttk.Entry(root)

        # Record the column index and item iid
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_iid = selected_iid

        entry_edit.insert(0, selected_text)
        entry_edit.select_range(0, tk.END)

        entry_edit.focus()

        entry_edit.bind("<FocusOut>", self.on_focus_out)
        entry_edit.bind("<Return>", self.on_enter_pressed)

        entry_edit.place(x=column_box[0], y=column_box[1], width=column_box[2], height=column_box[3])

    def on_enter_pressed(self, event):
        new_text = event.widget.get()

        # such as I002
        selected_iid = event.widget.editing_item_iid

        # Such as -1 (tree column), 0 (first self-defined column), etc.
        column_index = event.widget.editing_column_index

        if column_index == -1:
            self.item(selected_iid, text=new_text)
        else:
            current_values = self.item(selected_iid).get("values")
            current_values[column_index] = new_text
            self.item(selected_iid, values=current_values)
            print(current_values)

        event.widget.destroy()

    def on_focus_out(self, event):
        event.widget.destroy()


if __name__ == "__main__":

    root = tk.Tk()

    column_names = ("vehicle_name", "year", "colour")

    treeview_vehicles = TreeviewEdit(root, columns=column_names)
    treeview_vehicles.heading("#0", text="Vehicle Type")
    treeview_vehicles.heading("vehicle_name", text="Vehicle Name")
    treeview_vehicles.heading("year", text="Year")
    treeview_vehicles.heading("colour", text="Colour")

    sedan_row = treeview_vehicles.insert(parent="", index=tk.END, text="Sedan")  # add the parent

    treeview_vehicles.insert(parent=sedan_row, index=tk.END, values=("Nissan Versa", "2010", "Silver"))
    treeview_vehicles.insert(parent=sedan_row, index=tk.END, values=("Toyota Camry", "2012", "Blue"))

    treeview_vehicles.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
