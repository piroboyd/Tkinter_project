import tkinter as tk
from tkinter import ttk
import os


class Etykieta:
    def __init__(self, file_path):

        self.file_path = file_path
        self.filename = os.path.basename(file_path)
        parts = self.filename.split('_')

        self.marka = parts[0]
        self.nazwa_produktu = parts[1]
        self.waga = parts[2]
        self.smak = parts[3]
        self.wymiary_etykiety = parts[4]
        self.nazwa_waga_smak = f"{self.nazwa_produktu}_{self.waga}_{self.smak}_{self.wymiary_etykiety}"

        if "_back_" in self.filename:
            self.tyl = True
            self.nazwa_waga_smak = f"{self.nazwa_produktu}_{self.waga}_{self.smak}_back_{self.wymiary_etykiety}"
        if "MP-M" in self.filename:
            self.material = "Metalizowany podkład, fioletowy pantone na biały kolor - MAT"
        if "BFP-M" in self.filename:
            self.material = "Biała folia poliprenowa - MAT"


def list_files(directory):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files


def update_listbox_by_brand():
    # Pobierz aktualną wartość z comboboxa
    marka_z_comboboxa = combo.get()

    # Usuń aktualną zawartość listboxa
    listbox1.delete(0, tk.END)

    # Dodaj nowe elementy do listboxa, które odpowiadają wybranej marce w comboboxie
    for label_object in list_of_labels_objects:
        if (label_object.marka == marka_z_comboboxa):
            listbox1.insert(tk.END, label_object.nazwa_waga_smak)


# Sztywny katalog do testów
DIRECTORY = "G:\pythonik\katalogi etykiet do projektu tkinter\SFD_test"

# Making instance of window, setting resolution, title, icon, and bg colour.
window_height = 420
window_width = 420
window = tk.Tk()
window.geometry(f"{window_height}x{window_width}")
window.title("Etykieciarz")
icon = tk.PhotoImage(file="grafika/logo.png")
window.iconphoto(True, icon)
window.config(background="#c8c7d1")


def my_Click():
    myLabel = tk.Label(window, text="Look, I've clicked a button!", bg="red")
    myLabel.pack()


myButton = tk.Button(window, text="Click me!", padx=50, pady=20, command=my_Click, fg="black", bg="white")
myButton.pack()

# Creating a Label widget
# myLabel1 = Label(window, text="Hello World!")
# myLabel2 = Label(window, text="My name is Pirone")
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# myButton.pack()

# Pętla for, iterująca po plikach z danego katalogu, tworząca obiekty klasy Etykieta dla każdego pliku,
# Na końcu tworzymy listboxa z tymi etykietami.
list_of_files_paths = list_files(DIRECTORY)
list_of_labels_objects = []

for file in list_of_files_paths:
    etykieta = Etykieta(file)
    list_of_labels_objects.append(etykieta)

listbox1 = tk.Listbox(window)
listbox1.pack(fill="both", expand=False)

for label_object in list_of_labels_objects:
    listbox1.insert(tk.END, label_object.nazwa_waga_smak)


# CREATING A BOX WITH A LIST OF AVAILABLE PRODUCT BRANDS

# First, we create a list of brands by pulling it from each label, iterating over every label,
# then I convert it to a set to remove the repetitions and back to a list so I can sort it alphabetically and have the
# access to items to set the default value in the combobox later.
dostepne_marki = sorted(list(set([x.marka for x in list_of_labels_objects])))

combo = ttk.Combobox(window, values=dostepne_marki, state="readonly")  # utworzenie obiektu Combobox
combo.set("Wybierz markę etykiet")  # ustawienie wartości domyślnej
combo.bind("<<ComboboxSelected>>", lambda event: update_listbox_by_brand())
combo.pack()  # pakowanie Combobox na ekran



def update_listbox_by_productname():
    listbox_values = listbox1.get(0, "end")
    chosen_brand = combo.get()

    list_of_products_by_name = []

    for elements in listbox_values:
        if elements


# dostepne_produkty = sorted(list(set([x.nazwa_produktu for x in list_of_labels_objects])))
#
# combo2 = ttk.Combobox(window, values=dostepne_produkty, state="readonly") # utworzenie obiektu Combobox
# combo2.set("Wybierz produkt") # ustawienie wartości domyślnej
# combo2.bind("<<ComboboxSelected>>", lambda event: update_products())
# combo2.pack() # pakowanie Combobox na ekran
#

# window.mainloop()  # Place window on computer screen