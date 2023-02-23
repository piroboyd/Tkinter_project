import tkinter as tk
from tkinter import ttk
import os


class Etykieta:
    def __init__(self, file_path):

        self.file_path = file_path
        self.filename = os.path.basename(file_path).lower()
        parts = self.filename.split('_')

        self.marka = parts[0].upper()
        self.nazwa_produktu = parts[1]
        self.waga = parts[2]
        self.smak = parts[3]
        self.wymiary_etykiety = parts[4]
        self.nazwa_waga_smak = f"{self.nazwa_produktu}_{self.waga}_{self.smak}_{self.wymiary_etykiety}"

        if "_back_" in self.filename:
            self.tyl = True
            self.nazwa_waga_smak = f"{self.nazwa_produktu}_{self.waga}_{self.smak}_{self.wymiary_etykiety}_back"
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


def update_listbox_by_brand_and_update_combo2():
    # Pobierz aktualną wartość z comboboxa
    marka_z_comboboxa = combo_brand.get()

    # Usuń aktualną zawartość listboxa
    main_listbox.delete(0, tk.END)

    # Dodaj nowe elementy do listboxa, które odpowiadają wybranej marce w comboboxie
    for label_object in list_of_labels_objects:
        if label_object.marka == marka_z_comboboxa:
            main_listbox.insert(tk.END, label_object.nazwa_waga_smak)

    wybrana_marka_w_combo = combo_brand.get()
    dostepne_produkty = sorted(
        list(set([x.nazwa_produktu for x in list_of_labels_objects if x.marka == wybrana_marka_w_combo])))
    combo2_product.config(values=dostepne_produkty)


def update_listbox_by_product_and_update_combo_3():
    # Pobierz aktualną wartość z comboboxa
    produkt_z_comboboxa = combo2_product.get()

    # Usuń aktualną zawartość listboxa
    main_listbox.delete(0, tk.END)

    # Dodaj nowe elementy do listboxa, które odpowiadają wybranej marce w comboboxie
    for label_object in list_of_labels_objects:
        if (label_object.marka == combo_brand.get()) and (label_object.nazwa_produktu == combo2_product.get()):
            main_listbox.insert(tk.END, label_object.nazwa_waga_smak)

    wybrany_produkt_w_combo2 = combo2_product.get()
    dostepne_wagi = sorted(
        list(set([x.waga for x in list_of_labels_objects if x.marka == combo_brand.get() and
                  x.nazwa_produktu == wybrany_produkt_w_combo2])))
    combo3_weight.config(values=dostepne_wagi)


def update_listbox_by_weight():
    # Pobierz aktualną wartość z comboboxa
    waga_z_comboboxa = combo3_weight.get()

    # Usuń aktualną zawartość listboxa
    main_listbox.delete(0, tk.END)

    # Dodaj nowe elementy do listboxa, które odpowiadają wybranej marce w comboboxie
    for label_object in list_of_labels_objects:
        if (label_object.marka == combo_brand.get()) and (label_object.nazwa_produktu == combo2_product.get() and
                                                          (label_object.waga == combo3_weight.get())):
            main_listbox.insert(tk.END, label_object.nazwa_waga_smak)


def move_items_to_print_listbox():
    """Funkcja przenosząca zaznaczone elementy z Listboxa 1 do Listboxa 2."""
    selection_indices = main_listbox.curselection()

    # Przechodzenie po zaznaczonych elementach w Listboxie 1
    for index in selection_indices:
        value = main_listbox.get(index)
        # Sprawdzanie, czy wartość już istnieje w Listboxie 2
        if value not in print_listbox.get(0, tk.END):
            print_listbox.insert(tk.END, value)


def delete_items_from_print_listbox():
    # Funkcja usuwająca elementy z listboxa print_listbox

    # Funkcja usuwająca elementy z listboxa print
    selection_indices = print_listbox.curselection()

    # Usuwanie zaznaczonych elementów w odwrotnej kolejności, odwrotna bo normalne usuwanie zmienia indeksy.
    for index in reversed(selection_indices):
        print_listbox.delete(index)


# Sztywny katalog do testów
DIRECTORY = r"G:\pythonik\katalogi etykiet do projektu tkinter\test"

# Making instance of window, setting resolution, title, icon, and bg colour.
window_height = 400
window_width = 1000
window = tk.Tk()
window.geometry(f"{window_width}x{window_height}")
window.title("Etykieciarz")
icon = tk.PhotoImage(file="grafika/logo.png")
window.iconphoto(True, icon)
window.config(background="#c8c7d1")

for i in range(0, 8):
    window.columnconfigure(i, weight=1)

for i in range(0, 13):
    window.rowconfigure(i, weight=1)

# Pętla for, iterująca po plikach z danego katalogu, tworząca obiekty klasy Etykieta dla każdego pliku,
# Na końcu tworzymy listę i listboxa z tymi etykietami.
list_of_files_paths = list_files(DIRECTORY)
list_of_labels_objects = []

for file in list_of_files_paths:
    etykieta = Etykieta(file)
    list_of_labels_objects.append(etykieta)

# Tworzenie lewej ramki, i dodanie do niej main_listboxa razem z scrollbarem i etykietami.
main_listbox_row = 1

# main_listbox = tk.Listbox(window, width=40, height=20, selectmode=tk.EXTENDED)

main_listbox = tk.Listbox(window, selectmode=tk.EXTENDED)
main_listbox.grid(row=2, column=2, rowspan=10, columnspan=2, sticky="NS")

my_scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=main_listbox.yview)
my_scrollbar.grid(row=2, column=3, rowspan=10, sticky="NS")

main_listbox.config(yscrollcommand=my_scrollbar.set)

for label_object in list_of_labels_objects:
    main_listbox.insert(tk.END, label_object.nazwa_waga_smak)

# CREATING A BOX WITH A LIST OF AVAILABLE PRODUCT BRANDS

# First, we create a list of brands by pulling it from each label, iterating over every label,
# then I convert it to a set to remove the repetitions and back to a list so I can sort it alphabetically and have the
# access to items to set the default value in the combobox later.
dostepne_marki = sorted(list(set([x.marka for x in list_of_labels_objects])))

# Tworzenie frame dla combobuttonów
# left_frame_for_combobuttons = tk.Frame(window)
# left_frame_for_combobuttons.grid(row=1, column=0, sticky="EW")

combo_brand = ttk.Combobox(window, values=dostepne_marki, state="readonly")  # utworzenie obiektu Combobox
combo_brand.set("Wybierz markę etykiet")  # ustawienie wartości domyślnej
combo_brand.bind("<<ComboboxSelected>>", lambda event: update_listbox_by_brand_and_update_combo2())
combo_brand.grid(row=5, column=1, padx=5, pady=5)

combo2_product = ttk.Combobox(window, values=[], state="readonly")  # utworzenie obiektu Combobox
combo2_product.set("Wybierz produkt")  # ustawienie wartości domyślnej
combo2_product.bind("<<ComboboxSelected>>", lambda event: update_listbox_by_product_and_update_combo_3())
combo2_product.grid(row=6, column=1, padx=5, pady=5)

combo3_weight = ttk.Combobox(window, values=[], state="readonly")  # utworzenie obiektu Combobox
combo3_weight.set("Wybierz wagę")  # ustawienie wartości domyślnej
combo3_weight.bind("<<ComboboxSelected>>", lambda event: update_listbox_by_weight())
combo3_weight.grid(row=7, column=1, padx=5, pady=5)

# Ustawianie print_listboxa po prawej stronie aplikacji, razem z scrollbarem

print_listbox = tk.Listbox(window, selectmode=tk.EXTENDED)
print_listbox.grid(row=2, column=5, rowspan=10, columnspan=2, sticky="NS")

print_scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=print_listbox.yview)
print_scrollbar.grid(row=2, column=6, rowspan=10, sticky="NS")

print_listbox.config(yscrollcommand=print_scrollbar.set)

# Dodawanie buttonów do dodawania i usuwania etykiet razem z ich gridem.

# Add
add_to_print_button = tk.Button(window, text="Wrzuć etykiety do koszyka drukowania\n"
                                             ">>>>>>",
                                command=move_items_to_print_listbox)
add_to_print_button.grid(row=9, column=4)

# Remove
remove_from_print_button = tk.Button(window, text="Usuń etykiety z koszyka drukowania\n"
                                                  "<<<<<<",
                                     command=delete_items_from_print_listbox)
remove_from_print_button.grid(row=10, column=4)

window.mainloop()  # Place window on computer screen