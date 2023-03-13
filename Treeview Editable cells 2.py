import tkinter as tk
from tkinter import ttk
import random


class PrintTreeview(ttk.Treeview):
    # Tworzę klasę PrintTreeview, która ma dziedziczyć z klasy nadrzędnej "ttk.Treeview".
    # Tworzenie ttk. Treeview wymaga podania zmiennej container gdzie ma być przechowywany ten treeview:
    # tree = ttk.Treeview(container, **options)
    # oraz różnych zmiennych options, typu np columny, headings i inne opcje konfiguracyjne, dlatego też
    # używam zmiennych "master" jak containera oraz "**kwargs",
    # bo realnie nie wiem ile opcji konfiguracyjnych potem przekażę.
    # następnie metoda super wywołuje konstruktor klasy nadrzędnej (ttk. treeview) i inicjuje jej właściwości, dzięki
    # czemu PrintTreeview odziedziczy wszystko z "ttk.Treeview"
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        # Dla całego obiektu PrintTreeview, odpal metodę "onDoubleClick" kiedy user kliknie dwukrotnie gdziekolwiek w
        # widżecie.
        self.bind("<Double-Button-1>", self.onDoubleClick)

    def onDoubleClick(self, event):

        # Zidentyfikuj region na który klika user, jeśli nie jest to "cell", zakończ (return).
        identified_region = self.identify_region(event.x, event.y)
        if identified_region != "cell":
            return

        # Zidentyfikuj kolumnę na którą klika user i zamień output na int, żeby można było go potem użyć.
        column = self.identify_column(event.x)
        column_index = int(column[1:])

        # Metoda JobinPy
        # selected_iid = self.focus()
        # print(selected_iid)

        # Zidentyfikuj rząd na który klika user i zwróć wszystkie values dla rzędu, na który klika user.
        row_index = self.identify_row(event.y)
        selected_values = self.item(row_index)

        # print(f"rząd: {row_index}")
        # print(f"kolumna: {column_index}")
        # print(f"wszystkie values dla rzędu: {selected_values}")

        if column_index == 2:
            selected_amount = selected_values.get("values")

            print(selected_amount[1])


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Treeview test")
    root.geometry("620x200")

    # zdefiniuj kolumny, to co tu użyjesz nie będzie widoczne dla usera, to tak jakby ID tych kolumn
    columns = ["product_name", "amount"]

    # Stwórz obiekt PrintTreeview, dziedziczący po ttk.Treeview. Przekaż do obiektu kolumny ze zmiennej "columns",
    # a opcja show="headings" sprawia że będą widoczne wszystkie nagłówki poza tym pierwszym, z indeksami,
    # który nie jest nam potrzebny do niczego (dalej można korzystać z tych indeksów,
    # jedynie ta kolumna nie zostanie wyświetlona)
    print_treeview = PrintTreeview(root, columns=columns, show="headings")

    # Stwórz nagłówki, pierwszy nagłówek, domyślny został schowany dzięki show="headings" wcześniej.
    print_treeview.heading("#0", text="")
    print_treeview.heading("product_name", text="Etykieta")
    print_treeview.heading("amount", text="Ilość")

    # Wypełnij treeview przykładowymi danymi.
    contacts = []
    for n in range(1, 100):
        contacts.append((f'Etykieta_{n}', f"{random.randint(1,50)}"))

    for contact in contacts:
        print_treeview.insert('', tk.END, values=contact)


    print_treeview.grid(row=0, column=0, sticky='nsew')

    # run the app
    root.mainloop()