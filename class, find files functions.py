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

        if "_back_" in self.filename:
            self.tyl = True
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


DIRECTORY = "G:\pythonik\katalogi etykiet do projektu tkinter\SFD_test"

list_of_files = list_files(DIRECTORY)

# print(list_of_files)

list_of_labels_objects = []

for files in list_of_files:
    etykieta = Etykieta(files)
    list_of_labels_objects.append(etykieta)


# WYSWIETL LISTĘ MAREK PO PLIKACH
list_of_brands = set()

for element in list_of_labels_objects:
    list_of_brands.add(element.marka)

