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
window_height = 420
window_width = 420
window = tk.Tk()
window.geometry(f"{window_height}x{window_width}")
window.title("Etykieciarz")
icon = tk.PhotoImage(file="grafika/logo.png")
window.iconphoto(True, icon)
window.config(background="#c8c7d1")


def my_Click():
    myLabel = tk.Label(window, text="No i co klikasz baranie", bg="red")
    myLabel.pack()


myButton = tk.Button(window, text="Kliknij!", padx=50, pady=20, command=my_Click, fg="black", bg="white")
myButton.pack()

# Pętla for, iterująca po plikach z danego katalogu, tworząca obiekty klasy Etykieta dla każdego pliku,
# Na końcu tworzymy listę i listboxa z tymi etykietami.
list_of_files_paths = list_files(DIRECTORY)
list_of_labels_objects = []

for file in list_of_files_paths:
    etykieta = Etykieta(file)
    list_of_labels_objects.append(etykieta)

left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

main_listbox = tk.Listbox(left_frame, width=40, height=20, selectmode=tk.EXTENDED)
main_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=main_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

main_listbox.config(yscrollcommand=scrollbar.set)

for label_object in list_of_labels_objects:
    main_listbox.insert(tk.END, label_object.nazwa_waga_smak)

# def update_combo2():
#     wybrana_marka_w_combo = combo.get()
#     dostepne_produkty = sorted(
#         list(set([x.nazwa_produktu for x in list_of_labels_objects if x.marka == wybrana_marka_w_combo])))
#     combo2.config(values=dostepne_produkty)


# CREATING A BOX WITH A LIST OF AVAILABLE PRODUCT BRANDS

# First, we create a list of brands by pulling it from each label, iterating over every label,
# then I convert it to a set to remove the repetitions and back to a list so I can sort it alphabetically and have the
# access to items to set the default value in the combobox later.
dostepne_marki = sorted(list(set([x.marka for x in list_of_labels_objects])))

combo_brand = ttk.Combobox(window, values=dostepne_marki, state="readonly")  # utworzenie obiektu Combobox
combo_brand.set("Wybierz markę etykiet")  # ustawienie wartości domyślnej
combo_brand.bind("<<ComboboxSelected>>", lambda event: update_listbox_by_brand_and_update_combo2())
# combo.bind("<<ComboboxSelected>>", lambda event: update_combo2())
combo_brand.pack()  # pakowanie Combobox na ekran

combo2_product = ttk.Combobox(window, values=[], state="readonly")  # utworzenie obiektu Combobox
combo2_product.set("Wybierz produkt")  # ustawienie wartości domyślnej
combo2_product.bind("<<ComboboxSelected>>", lambda event: update_listbox_by_product_and_update_combo_3())
combo2_product.pack()  # pakowanie Combobox na ekran

combo3_weight = ttk.Combobox(window, values=[], state="readonly")  # utworzenie obiektu Combobox
combo3_weight.set("Wybierz wagę")  # ustawienie wartości domyślnej
combo3_weight.bind("<<ComboboxSelected>>", lambda event: update_listbox_by_weight())
combo3_weight.pack()  # pakowanie Combobox na ekran

# Ustawianie print_listboxa po prawej stronie aplikacji, razem z scrollbarem
right_frame = tk.Frame(window)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

print_listbox = tk.Listbox(right_frame, selectmode=tk.EXTENDED, width=40, height=20)
print_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=print_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

print_listbox.config(yscrollcommand=scrollbar.set)


# Dodawanie buttonów do dodawania i usuwania etykiet.

# Add
add_to_print_button = tk.Button(window, text="Wrzuć etykiety do koszyka drukowania\n"
                                             ">>>>>>",
                                command=move_items_to_print_listbox)
add_to_print_button.pack()

# Remove
remove_from_print_button = tk.Button(window, text="Usuń etykiety z koszyka drukowania\n"
                                                  "<<<<<<",
                                     command=delete_items_from_print_listbox)
remove_from_print_button.pack()




window.mainloop()  # Place window on computer screen
