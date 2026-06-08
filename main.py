from tkinter import *
from tkinter import ttk
import tkintermapview
from model import biblioteki, klienci, pracownicy, ksiazki, wypozyczenia
from controller import get_coordinates

edit_index = None
edit_client_index = None
edit_employee_index = None
edit_book_index = None

markers = []
client_markers = []
employee_markers = []


# BIBLIOTEKI

def refresh_biblioteki_combobox():

    biblioteki_nazwy = [
        b["nazwa"]
        for b in biblioteki
    ]

    combo_biblioteka["values"] = biblioteki_nazwy
    combo_biblioteka_pracownik["values"] = biblioteki_nazwy
    combo_biblioteka_ksiazka["values"] = biblioteki_nazwy
    combo_filtr_klienci["values"] = biblioteki_nazwy
    combo_filtr_pracownicy["values"] = biblioteki_nazwy
    combo_filtr_ksiazki["values"] = biblioteki_nazwy

def show_biblioteka_details():
    i = lista_bibliotek.index(ACTIVE)

    nazwa = biblioteki[i]["nazwa"]
    miasto = biblioteki[i]["miasto"]

    label_nazwa.config(text=nazwa)
    label_miasto.config(text=miasto)


    map_widget.set_position(
        biblioteki[i]["lat"],
        biblioteki[i]["lon"]
    )

    map_widget.set_zoom(12)


def edit_biblioteka():
    global edit_index

    edit_index = lista_bibliotek.curselection()[0]

    entry_nazwa.delete(0, END)
    entry_miasto.delete(0, END)

    entry_nazwa.insert(
        0,
        biblioteki[edit_index]["nazwa"]
    )

    entry_miasto.insert(
        0,
        biblioteki[edit_index]["miasto"]
    )

    refresh_biblioteki_combobox()

def delete_biblioteka():
    i = lista_bibliotek.curselection()[0]

    markers[i].delete()
    markers.pop(i)

    biblioteki.pop(i)

    lista_bibliotek.delete(i)




def add_biblioteka():
    global edit_index
    nazwa = entry_nazwa.get()
    miasto = entry_miasto.get()

    coordinates = get_coordinates(miasto)

    if edit_index is None:

        biblioteki.append({
            "nazwa": nazwa,
            "miasto": miasto,
            "lat": coordinates[0],
            "lon": coordinates[1]
        })

        lista_bibliotek.insert(
            END,
            nazwa
        )

        marker = map_widget.set_marker(
            coordinates[0],
            coordinates[1],
            text=nazwa
        )

        markers.append(marker)
    else:

        biblioteki[edit_index] = {
            "nazwa": nazwa,
            "miasto": miasto,
            "lat": coordinates[0],
            "lon": coordinates[1]
        }

        lista_bibliotek.delete(edit_index)
        lista_bibliotek.insert(edit_index, nazwa)

        markers[edit_index].delete()

        markers[edit_index] = map_widget.set_marker(
            coordinates[0],
            coordinates[1],
            text=nazwa
        )
        edit_index = None

    entry_nazwa.delete(0, END)
    entry_miasto.delete(0, END)

    refresh_biblioteki_combobox()

# KLIENCI


def filter_klienci():

    biblioteka = combo_filtr_klienci.get()

    lista_klientow.delete(0, END)

    for marker in client_markers:
        marker.delete()

    client_markers.clear()

    for klient in klienci:

        if klient["biblioteka"] == biblioteka:

            lista_klientow.insert(
                END,
                f"{klient['imie']} {klient['nazwisko']}"
            )

            marker = map_widget_klienci.set_marker(
                klient["lat"],
                klient["lon"],
                text=f"{klient['imie']} {klient['nazwisko']}"
            )

            client_markers.append(marker)


def show_all_klienci():

    lista_klientow.delete(0, END)

    for marker in client_markers:
        marker.delete()

    client_markers.clear()

    for klient in klienci:

        lista_klientow.insert(
            END,
            f"{klient['imie']} {klient['nazwisko']}"
        )

        marker = map_widget_klienci.set_marker(
            klient["lat"],
            klient["lon"],
            text=f"{klient['imie']} {klient['nazwisko']}"
        )

        client_markers.append(marker)
def delete_klient():
    i = lista_klientow.curselection()[0]

    client_markers[i].delete()
    client_markers.pop(i)

    klienci.pop(i)

    lista_klientow.delete(i)

def refresh_klienci_combobox():

    combo_klient["values"] = [
        f"{k['imie']} {k['nazwisko']}"
        for k in klienci
    ]

def show_klient_details():
    i = lista_klientow.curselection()[0]

    klient = klienci[i]

    label_imie_wartosc.config(
        text=klient["imie"]
    )

    label_nazwisko_wartosc.config(
        text=klient["nazwisko"]
    )

    label_miasto_wartosc.config(
        text=klient["miasto"]
    )

    label_biblioteka_wartosc.config(
        text=klient["biblioteka"]
    )

    map_widget_klienci.set_position(
        klient["lat"],
        klient["lon"]
    )

    map_widget_klienci.set_zoom(12)


def edit_klient():
    global edit_client_index

    edit_client_index = lista_klientow.curselection()[0]

    klient = klienci[edit_client_index]

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miasto_klient.delete(0, END)

    entry_imie.insert(0, klient["imie"])
    entry_nazwisko.insert(0, klient["nazwisko"])
    entry_miasto_klient.insert(0, klient["miasto"])

    combo_biblioteka.set(
        klient["biblioteka"]
    )
    refresh_klienci_combobox()


def add_klient():
    global edit_client_index

    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    miasto = entry_miasto_klient.get()
    biblioteka = combo_biblioteka.get()

    coordinates = get_coordinates(miasto)

    if edit_client_index is None:

        klient = {
            "imie": imie,
            "nazwisko": nazwisko,
            "miasto": miasto,
            "biblioteka": biblioteka,
            "lat": coordinates[0],
            "lon": coordinates[1]
        }

        klienci.append(klient)

        lista_klientow.insert(
            END,
            f"{imie} {nazwisko}"
        )

        marker = map_widget_klienci.set_marker(
            coordinates[0],
            coordinates[1],
            text=f"{imie} {nazwisko}"
        )

        client_markers.append(marker)

    else:

        klienci[edit_client_index] = {
            "imie": imie,
            "nazwisko": nazwisko,
            "miasto": miasto,
            "biblioteka": biblioteka,
            "lat": coordinates[0],
            "lon": coordinates[1]
        }

        lista_klientow.delete(edit_client_index)

        lista_klientow.insert(
            edit_client_index,
            f"{imie} {nazwisko}"
        )

        client_markers[edit_client_index].delete()

        client_markers[edit_client_index] = map_widget_klienci.set_marker(
            coordinates[0],
            coordinates[1],
            text=f"{imie} {nazwisko}"
        )

        edit_client_index = None
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miasto_klient.delete(0, END)

    combo_biblioteka.set("")
    refresh_klienci_combobox()

# PRACOWNICY

def filter_pracownicy():

    biblioteka = combo_filtr_pracownicy.get()

    lista_pracownikow.delete(0, END)

    for marker in employee_markers:
        marker.delete()

    employee_markers.clear()

    for pracownik in pracownicy:

        if pracownik["biblioteka"] == biblioteka:

            lista_pracownikow.insert(
                END,
                f"{pracownik['imie']} {pracownik['nazwisko']}"
            )

            marker = map_widget_pracownicy.set_marker(
                pracownik["lat"],
                pracownik["lon"],
                text=f"{pracownik['imie']} {pracownik['nazwisko']}"
            )

            employee_markers.append(marker)

def show_all_pracownicy():

    lista_pracownikow.delete(0, END)

    for marker in employee_markers:
        marker.delete()

    employee_markers.clear()

    for pracownik in pracownicy:

        lista_pracownikow.insert(
            END,
            f"{pracownik['imie']} {pracownik['nazwisko']}"
        )

        marker = map_widget_pracownicy.set_marker(
            pracownik["lat"],
            pracownik["lon"],
            text=f"{pracownik['imie']} {pracownik['nazwisko']}"
        )

        employee_markers.append(marker)


def delete_pracownik():
    i = lista_pracownikow.curselection()[0]

    employee_markers[i].delete()
    employee_markers.pop(i)

    pracownicy.pop(i)

    lista_pracownikow.delete(i)


def show_pracownik_details():
    i = lista_pracownikow.curselection()[0]

    pracownik = pracownicy[i]

    label_imie_pracownik_wartosc.config(
        text=pracownik["imie"]
    )

    label_nazwisko_pracownik_wartosc.config(
        text=pracownik["nazwisko"]
    )

    label_miasto_pracownik_wartosc.config(
        text=pracownik["miasto"]
    )

    label_biblioteka_pracownik_wartosc.config(
        text=pracownik["biblioteka"]
    )

    map_widget_pracownicy.set_position(
        pracownik["lat"],
        pracownik["lon"]
    )

    map_widget_pracownicy.set_zoom(12)


def edit_pracownik():
    global edit_employee_index

    edit_employee_index = lista_pracownikow.curselection()[0]

    pracownik = pracownicy[edit_employee_index]

    entry_imie_pracownik.delete(0, END)
    entry_nazwisko_pracownik.delete(0, END)
    entry_miasto_pracownik.delete(0, END)

    entry_imie_pracownik.insert(
        0,
        pracownik["imie"]
    )

    entry_nazwisko_pracownik.insert(
        0,
        pracownik["nazwisko"]
    )

    entry_miasto_pracownik.insert(
        0,
        pracownik["miasto"]
    )

    combo_biblioteka_pracownik.set(
        pracownik["biblioteka"]
    )


def add_pracownik():
    global edit_employee_index

    imie = entry_imie_pracownik.get()
    nazwisko = entry_nazwisko_pracownik.get()
    miasto = entry_miasto_pracownik.get()
    biblioteka = combo_biblioteka_pracownik.get()

    coordinates = get_coordinates(miasto)

    if edit_employee_index is None:

        pracownik = {
            "imie": imie,
            "nazwisko": nazwisko,
            "miasto": miasto,
            "biblioteka": biblioteka,
            "lat": coordinates[0],
            "lon": coordinates[1]
        }

        pracownicy.append(pracownik)

        lista_pracownikow.insert(
            END,
            f"{imie} {nazwisko}"
        )

        marker = map_widget_pracownicy.set_marker(
            coordinates[0],
            coordinates[1],
            text=f"{imie} {nazwisko}"
        )

        employee_markers.append(marker)

    else:

        pracownicy[edit_employee_index] = {
            "imie": imie,
            "nazwisko": nazwisko,
            "miasto": miasto,
            "biblioteka": biblioteka,
            "lat": coordinates[0],
            "lon": coordinates[1]
        }

        lista_pracownikow.delete(edit_employee_index)

        lista_pracownikow.insert(
            edit_employee_index,
            f"{imie} {nazwisko}"
        )

        employee_markers[edit_employee_index].delete()

        employee_markers[edit_employee_index] = map_widget_pracownicy.set_marker(
            coordinates[0],
            coordinates[1],
            text=f"{imie} {nazwisko}"
        )

        edit_employee_index = None

    entry_imie_pracownik.delete(0, END)
    entry_nazwisko_pracownik.delete(0, END)
    entry_miasto_pracownik.delete(0, END)

    combo_biblioteka_pracownik.set("")


# ksiazka

def filter_ksiazki():

    biblioteka = combo_filtr_ksiazki.get()

    lista_ksiazek.delete(0, END)

    for ksiazka in ksiazki:

        if ksiazka["biblioteka"] == biblioteka:

            lista_ksiazek.insert(
                END,
                ksiazka["tytul"]
            )


def show_all_ksiazki():

    lista_ksiazek.delete(0, END)

    for ksiazka in ksiazki:

        lista_ksiazek.insert(
            END,
            ksiazka["tytul"]
        )


def show_ksiazka_details():
    i = lista_ksiazek.curselection()[0]

    ksiazka = ksiazki[i]

    label_tytul.config(
        text=ksiazka["tytul"]
    )

    label_autor.config(
        text=ksiazka["autor"]
    )

    label_rok.config(
        text=ksiazka["rok"]
    )

    label_biblioteka_ksiazka.config(
        text=ksiazka["biblioteka"]
    )

def refresh_ksiazki_combobox():

    combo_ksiazka["values"] = [
        k["tytul"]
        for k in ksiazki
    ]

def delete_ksiazka():
    i = lista_ksiazek.curselection()[0]

    ksiazki.pop(i)

    lista_ksiazek.delete(i)


def edit_ksiazka():
    global edit_book_index

    edit_book_index = lista_ksiazek.curselection()[0]

    ksiazka = ksiazki[edit_book_index]

    entry_tytul.delete(0, END)
    entry_autor.delete(0, END)
    entry_rok.delete(0, END)

    entry_tytul.insert(
        0,
        ksiazka["tytul"]
    )

    entry_autor.insert(
        0,
        ksiazka["autor"]
    )

    entry_rok.insert(
        0,
        ksiazka["rok"]
    )

    combo_biblioteka_ksiazka.set(
        ksiazka["biblioteka"]
    )
    refresh_ksiazki_combobox()


def add_ksiazka():
    global edit_book_index

    tytul = entry_tytul.get()
    autor = entry_autor.get()
    rok = entry_rok.get()
    biblioteka = combo_biblioteka_ksiazka.get()

    if edit_book_index is None:

        ksiazka = {
            "tytul": tytul,
            "autor": autor,
            "rok": rok,
            "biblioteka": biblioteka
        }

        ksiazki.append(ksiazka)

        lista_ksiazek.insert(
            END,
            tytul
        )

    else:

        ksiazki[edit_book_index] = {
            "tytul": tytul,
            "autor": autor,
            "rok": rok,
            "biblioteka": biblioteka
        }

        lista_ksiazek.delete(edit_book_index)

        lista_ksiazek.insert(
            edit_book_index,
            tytul
        )

        edit_book_index = None

    entry_tytul.delete(0, END)
    entry_autor.delete(0, END)
    entry_rok.delete(0, END)

    combo_biblioteka_ksiazka.set("")
    refresh_ksiazki_combobox()

# wypozyczenie

def add_wypozyczenie():

    klient = combo_klient.get()
    ksiazka = combo_ksiazka.get()

    wypozyczenie = {
        "klient": klient,
        "ksiazka": ksiazka
    }

    wypozyczenia.append(
        wypozyczenie
    )

    lista_wypozyczen.insert(
        END,
        f"{klient} -> {ksiazka}"
    )

    combo_klient.set("")
    combo_ksiazka.set("")

def show_books_for_client():

    klient = combo_klient.get()

    lista_ksiazek_klienta.delete(0, END)

    for wypozyczenie in wypozyczenia:

        if wypozyczenie["klient"] == klient:

            lista_ksiazek_klienta.insert(
                END,
                wypozyczenie["ksiazka"]
            )

# GUI


root = Tk()
root.title("System zarządzania bibliotekami")
root.geometry("1200x800")
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

tab_biblioteki = Frame(notebook)
tab_klienci = Frame(notebook)
tab_pracownicy = Frame(notebook)
tab_ksiazki = Frame(notebook)
tab_wypozyczenia = Frame(notebook)

notebook.add(tab_biblioteki, text="Biblioteki")
notebook.add(tab_klienci, text="Klienci")
notebook.add(tab_pracownicy, text="Pracownicy")
notebook.add(tab_ksiazki, text="Książki")
notebook.add(tab_wypozyczenia, text="Wypożyczenia")

# BIBLIO RAMKI


ramka_lista = Frame(tab_biblioteki)
ramka_formularz = Frame(tab_biblioteki)
ramka_szczegoly = Frame(tab_biblioteki)
ramka_mapa = Frame(tab_biblioteki)

ramka_lista.grid(row=0, column=0, padx=20, pady=20)
ramka_formularz.grid(row=0, column=1, padx=20, pady=20)
ramka_szczegoly.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# KLIENCI RAMKI


ramka_lista_klienci = Frame(tab_klienci)
ramka_formularz_klienci = Frame(tab_klienci)
ramka_szczegoly_klienci = Frame(tab_klienci)
ramka_mapa_klienci = Frame(tab_klienci)

ramka_lista_klienci.grid(row=0, column=0, padx=20, pady=20)
ramka_formularz_klienci.grid(row=0, column=1, padx=20, pady=20)
ramka_szczegoly_klienci.grid(row=1, column=0, columnspan=2)
ramka_mapa_klienci.grid(row=2, column=0, columnspan=2)

# PRACOWNICY RAMKI


ramka_lista_pracownicy = Frame(tab_pracownicy)
ramka_formularz_pracownicy = Frame(tab_pracownicy)
ramka_szczegoly_pracownicy = Frame(tab_pracownicy)
ramka_mapa_pracownicy = Frame(tab_pracownicy)

ramka_lista_pracownicy.grid(row=0, column=0, padx=20, pady=20)
ramka_formularz_pracownicy.grid(row=0, column=1, padx=20, pady=20)
ramka_szczegoly_pracownicy.grid(row=1, column=0, columnspan=2)
ramka_mapa_pracownicy.grid(row=2, column=0, columnspan=2)

# KSIAZKI RAMKI

ramka_lista_ksiazki = Frame(tab_ksiazki)
ramka_formularz_ksiazki = Frame(tab_ksiazki)
ramka_szczegoly_ksiazki = Frame(tab_ksiazki)

ramka_lista_ksiazki.grid(row=0, column=0, padx=20, pady=20)
ramka_formularz_ksiazki.grid(row=0, column=1, padx=20, pady=20)
ramka_szczegoly_ksiazki.grid(row=1, column=0, columnspan=2)

# WYPOŻYCZENIA RAMKI

ramka_formularz_wypozyczenia = Frame(tab_wypozyczenia)
ramka_lista_wypozyczenia = Frame(tab_wypozyczenia)

ramka_formularz_wypozyczenia.grid(row=0, column=0, padx=20, pady=20)

ramka_lista_wypozyczenia.grid(row=1, column=0, padx=20, pady=20)

# BIBLIO LISTA

Label(ramka_lista, text="Lista bibliotek").grid(row=0, column=0)

lista_bibliotek = Listbox(ramka_lista, width=35, height=10)

lista_bibliotek.grid(row=1, column=0)

Button(ramka_lista,text="Pokaż szczegóły",command=show_biblioteka_details).grid(row=2, column=0)

Button(ramka_lista,text="Usuń bibliotekę",command=delete_biblioteka).grid(row=2, column=1)

Button(ramka_lista, text="Edytuj bibliotekę", command=edit_biblioteka).grid(row=2, column=2)

# KLIENT LISTA


Label(ramka_lista_klienci,text="Lista klientów").grid(row=0, column=0)

lista_klientow = Listbox(ramka_lista_klienci,width=35,height=10)

lista_klientow.grid(row=1, column=0)

Label(ramka_lista_klienci,text="Biblioteka:").grid(row=0, column=1)

combo_filtr_klienci = ttk.Combobox(
    ramka_lista_klienci,
    values=[b["nazwa"] for b in biblioteki],
    state="readonly",
    width=20
)

combo_filtr_klienci.grid(row=0, column=2)

Button(ramka_lista_klienci,text="Pokaż szczegóły",command=show_klient_details).grid(row=2, column=0)

Button(ramka_lista_klienci,text="Usuń klienta",command=delete_klient).grid(row=2, column=1)

Button(ramka_lista_klienci,text="Edytuj klienta",command=edit_klient).grid(row=2, column=2)

Button(ramka_lista_klienci, text="Filtruj",command=filter_klienci).grid(row=0, column=3)

Button(ramka_lista_klienci,text="Wszyscy",command=show_all_klienci).grid(row=0, column=4)

# PRACOWNIK LISTA


Label(ramka_lista_pracownicy,text="Lista pracowników").grid(row=0, column=0)

lista_pracownikow = Listbox(
    ramka_lista_pracownicy,
    width=35,
    height=10
)

lista_pracownikow.grid(row=1, column=0)

Button(
    ramka_lista_pracownicy,
    text="Pokaż szczegóły",
    command=show_pracownik_details
).grid(row=2, column=0)

Button(
    ramka_lista_pracownicy,
    text="Usuń pracownika",
    command=delete_pracownik
).grid(row=2, column=1)

Button(
    ramka_lista_pracownicy,
    text="Edytuj pracownika",
    command=edit_pracownik
).grid(row=2, column=2)

Label(ramka_lista_pracownicy, text="Biblioteka:").grid(row=0, column=1)

combo_filtr_pracownicy = ttk.Combobox(
    ramka_lista_pracownicy,
    values=[b["nazwa"] for b in biblioteki],
    state="readonly",
    width=20
)

combo_filtr_pracownicy.grid(row=0, column=2)

Button(
    ramka_lista_pracownicy,
    text="Filtruj",
    command=filter_pracownicy
).grid(row=0, column=3)

Button(
    ramka_lista_pracownicy,
    text="Wszyscy",
    command=show_all_pracownicy
).grid(row=0, column=4)

# KSIAZKI LISTA

Label(
    ramka_lista_ksiazki,
    text="Lista książek"
).grid(row=0, column=0)

lista_ksiazek = Listbox(
    ramka_lista_ksiazki,
    width=35,
    height=10
)

lista_ksiazek.grid(row=1, column=0)

Button(
    ramka_lista_ksiazki,
    text="Pokaż szczegóły",
    command=show_ksiazka_details
).grid(row=2, column=0)

Button(
    ramka_lista_ksiazki,
    text="Usuń książkę",
    command=delete_ksiazka
).grid(row=2, column=1)

Button(
    ramka_lista_ksiazki,
    text="Edytuj książkę",
    command=edit_ksiazka
).grid(row=2, column=2)

Label(ramka_lista_ksiazki, text="Biblioteka:").grid(row=0, column=1)

combo_filtr_ksiazki = ttk.Combobox(
    ramka_lista_ksiazki,
    values=[b["nazwa"] for b in biblioteki],
    state="readonly",
    width=20
)

combo_filtr_ksiazki.grid(row=0, column=2)

Button(
    ramka_lista_ksiazki,
    text="Filtruj",
    command=filter_ksiazki
).grid(row=0, column=3)

Button(
    ramka_lista_ksiazki,
    text="Wszyscy",
    command=show_all_ksiazki
).grid(row=0, column=4)


# WYPOŻYCZENIA LISTA

Label(
    ramka_lista_wypozyczenia,
    text="Lista wypożyczeń"
).grid(row=0, column=0)

lista_wypozyczen = Listbox(
    ramka_lista_wypozyczenia,
    width=60,
    height=10
)

lista_wypozyczen.grid(
    row=1,
    column=0
)

lista_ksiazek_klienta = Listbox(
    ramka_lista_wypozyczenia,
    width=40,
    height=8
)

lista_ksiazek_klienta.grid(
    row=3,
    column=0
)

# BIBLIO FORMULARZ


Label(
    ramka_formularz,
    text="Formularz biblioteki"
).grid(row=0, column=0, columnspan=2)

Label(
    ramka_formularz,
    text="Nazwa:"
).grid(row=1, column=0, sticky=W)

entry_nazwa = Entry(ramka_formularz)
entry_nazwa.grid(row=1, column=1)

Label(
    ramka_formularz,
    text="Miasto:"
).grid(row=2, column=0, sticky=W)

entry_miasto = Entry(ramka_formularz)
entry_miasto.grid(row=2, column=1)

Button(
    ramka_formularz,
    text="Dodaj bibliotekę",
    command=add_biblioteka
).grid(row=3, column=0, columnspan=2)

# KLIENT FORMULARZ

Label(
    ramka_formularz_klienci,
    text="Formularz klienta"
).grid(row=0, column=0, columnspan=2)

Label(
    ramka_formularz_klienci,
    text="Imię:"
).grid(row=1, column=0, sticky=W)

entry_imie = Entry(ramka_formularz_klienci)
entry_imie.grid(row=1, column=1)

Label(
    ramka_formularz_klienci,
    text="Nazwisko:"
).grid(row=2, column=0, sticky=W)

entry_nazwisko = Entry(ramka_formularz_klienci)
entry_nazwisko.grid(row=2, column=1)

Label(
    ramka_formularz_klienci,
    text="Miasto:"
).grid(row=3, column=0, sticky=W)

entry_miasto_klient = Entry(
    ramka_formularz_klienci
)

entry_miasto_klient.grid(row=3, column=1)

Label(
    ramka_formularz_klienci,
    text="Biblioteka:"
).grid(row=4, column=0, sticky=W)
biblioteki_nazwy = []

for biblioteka in biblioteki:
    biblioteki_nazwy.append(
        biblioteka["nazwa"]
    )

combo_biblioteka = ttk.Combobox(
    ramka_formularz_klienci,
    values=biblioteki_nazwy,
    state="readonly"
)

combo_biblioteka.grid(row=4, column=1)

Button(
    ramka_formularz_klienci,
    text="Dodaj klienta",
    command=add_klient
).grid(row=5, column=0, columnspan=2)

# PRACONWIK FORMULARZ
Label(
    ramka_formularz_pracownicy,
    text="Formularz pracownika"
).grid(row=0, column=0, columnspan=2)

Label(
    ramka_formularz_pracownicy,
    text="Imię:"
).grid(row=1, column=0)

entry_imie_pracownik = Entry(
    ramka_formularz_pracownicy
)

entry_imie_pracownik.grid(row=1, column=1)

Label(
    ramka_formularz_pracownicy,
    text="Nazwisko:"
).grid(row=2, column=0)

Label(
    ramka_formularz_pracownicy,
    text="Biblioteka:"
).grid(row=4, column=0)
entry_nazwisko_pracownik = Entry(
    ramka_formularz_pracownicy
)

entry_nazwisko_pracownik.grid(row=2, column=1)

Label(
    ramka_formularz_pracownicy,
    text="Miasto:"
).grid(row=3, column=0)

entry_miasto_pracownik = Entry(
    ramka_formularz_pracownicy
)

entry_miasto_pracownik.grid(row=3, column=1)

combo_biblioteka_pracownik = ttk.Combobox(
    ramka_formularz_pracownicy,
    values=[b["nazwa"] for b in biblioteki],
    state="readonly"
)

combo_biblioteka_pracownik.grid(row=4, column=1)

Button(
    ramka_formularz_pracownicy,
    text="Dodaj pracownika",
    command=add_pracownik
).grid(row=5, column=0, columnspan=2)

# KSIAZKI FORMULARZ

Label(
    ramka_formularz_ksiazki,
    text="Formularz książki"
).grid(row=0, column=0, columnspan=2)

Label(
    ramka_formularz_ksiazki,
    text="Tytuł:"
).grid(row=1, column=0)

entry_tytul = Entry(
    ramka_formularz_ksiazki
)

entry_tytul.grid(row=1, column=1)

Label(
    ramka_formularz_ksiazki,
    text="Autor:"
).grid(row=2, column=0)

entry_autor = Entry(
    ramka_formularz_ksiazki
)

entry_autor.grid(row=2, column=1)

Label(
    ramka_formularz_ksiazki,
    text="Rok:"
).grid(row=3, column=0)

entry_rok = Entry(
    ramka_formularz_ksiazki
)

entry_rok.grid(row=3, column=1)

Label(
    ramka_formularz_ksiazki,
    text="Biblioteka:"
).grid(row=4, column=0)

combo_biblioteka_ksiazka = ttk.Combobox(
    ramka_formularz_ksiazki,
    values=[b["nazwa"] for b in biblioteki],
    state="readonly"
)

combo_biblioteka_ksiazka.grid(row=4, column=1)

Button(
    ramka_formularz_ksiazki,
    text="Dodaj książkę",
    command=add_ksiazka
).grid(row=5, column=0, columnspan=2)

# WYPOŻYCZENIA FORMULARZ

Label(
    ramka_formularz_wypozyczenia,
    text="Klient:"
).grid(row=0, column=0)
combo_klient = ttk.Combobox(
    ramka_formularz_wypozyczenia,
    values=[
        f"{k['imie']} {k['nazwisko']}"
        for k in klienci
    ],
    state="readonly"
)

combo_klient.grid(
    row=0,
    column=1
)

Label(
    ramka_formularz_wypozyczenia,
    text="Książka:"
).grid(row=1, column=0)

combo_ksiazka = ttk.Combobox(
    ramka_formularz_wypozyczenia,
    values=[
        k["tytul"]
        for k in ksiazki
    ],
    state="readonly"
)

combo_ksiazka.grid(
    row=1,
    column=1
)
Button(
    ramka_formularz_wypozyczenia,
    text="Wypożycz książkę",
    command=add_wypozyczenie
).grid(
    row=2,
    column=0,
    columnspan=2
)

Button(
    ramka_formularz_wypozyczenia,
    text="Pokaż książki klienta",
    command=show_books_for_client
).grid(
    row=3,
    column=0,
    columnspan=2
)

# BIBLIO SCZEGÓŁY

Label(ramka_szczegoly,text="Szczegóły biblioteki").grid(row=0, column=0)

Label(ramka_szczegoly,text="Nazwa:").grid(row=1, column=0)

label_nazwa = Label(ramka_szczegoly,text="...")

label_nazwa.grid(row=1, column=1)

Label(ramka_szczegoly,text="Miasto:").grid(row=2, column=0)

label_miasto = Label(ramka_szczegoly,text="...")

label_miasto.grid(row=2, column=1)


# KLIENT SZCZEGOLY

Label(
    ramka_szczegoly_klienci,
    text="Szczegóły klienta"
).grid(row=0, column=0)

Label(
    ramka_szczegoly_klienci,
    text="Imię:"
).grid(row=1, column=0)

label_imie_wartosc = Label(
    ramka_szczegoly_klienci,
    text="..."
)

label_imie_wartosc.grid(row=1, column=1)

Label(
    ramka_szczegoly_klienci,
    text="Nazwisko:"
).grid(row=1, column=2)

label_nazwisko_wartosc = Label(
    ramka_szczegoly_klienci,
    text="..."
)

label_nazwisko_wartosc.grid(row=1, column=3)

Label(
    ramka_szczegoly_klienci,
    text="Miasto:"
).grid(row=1, column=4)

label_miasto_wartosc = Label(
    ramka_szczegoly_klienci,
    text="..."
)

label_miasto_wartosc.grid(row=1, column=5)

Label(
    ramka_szczegoly_klienci,
    text="Biblioteka:"
).grid(row=1, column=6)

label_biblioteka_wartosc = Label(
    ramka_szczegoly_klienci,
    text="..."
)

label_biblioteka_wartosc.grid(row=1, column=7)

# SZCZEGOLY PRACOWNIK

Label(
    ramka_szczegoly_pracownicy,
    text="Szczegóły pracownika"
).grid(row=0, column=0)

Label(
    ramka_szczegoly_pracownicy,
    text="Imię:"
).grid(row=1, column=0)

label_imie_pracownik_wartosc = Label(
    ramka_szczegoly_pracownicy,
    text="..."
)

label_imie_pracownik_wartosc.grid(row=1, column=1)

Label(
    ramka_szczegoly_pracownicy,
    text="Nazwisko:"
).grid(row=1, column=2)

label_nazwisko_pracownik_wartosc = Label(
    ramka_szczegoly_pracownicy,
    text="..."
)

label_nazwisko_pracownik_wartosc.grid(row=1, column=3)

Label(
    ramka_szczegoly_pracownicy,
    text="Miasto:"
).grid(row=1, column=4)

label_miasto_pracownik_wartosc = Label(
    ramka_szczegoly_pracownicy,
    text="..."
)

label_miasto_pracownik_wartosc.grid(row=1, column=5)

Label(
    ramka_szczegoly_pracownicy,
    text="Biblioteka:"
).grid(row=1, column=6)

label_biblioteka_pracownik_wartosc = Label(
    ramka_szczegoly_pracownicy,
    text="..."
)

label_biblioteka_pracownik_wartosc.grid(row=1, column=7)

# KSIAZKI SZCZEGOLY

Label(
    ramka_szczegoly_ksiazki,
    text="Szczegóły książki"
).grid(row=0, column=0)

Label(
    ramka_szczegoly_ksiazki,
    text="Tytuł:"
).grid(row=1, column=0)

label_tytul = Label(
    ramka_szczegoly_ksiazki,
    text="..."
)

label_tytul.grid(row=1, column=1)

Label(
    ramka_szczegoly_ksiazki,
    text="Autor:"
).grid(row=1, column=2)

label_autor = Label(
    ramka_szczegoly_ksiazki,
    text="..."
)

label_autor.grid(row=1, column=3)

Label(
    ramka_szczegoly_ksiazki,
    text="Rok:"
).grid(row=1, column=4)

label_rok = Label(
    ramka_szczegoly_ksiazki,
    text="..."
)

label_rok.grid(row=1, column=5)

Label(
    ramka_szczegoly_ksiazki,
    text="Biblioteka:"
).grid(row=1, column=6)

label_biblioteka_ksiazka = Label(
    ramka_szczegoly_ksiazki,
    text="..."
)

label_biblioteka_ksiazka.grid(row=1, column=7)

# BIBLIO MAPA


map_widget = tkintermapview.TkinterMapView(
    ramka_mapa,
    width=1000,
    height=500
)

map_widget.grid(row=0, column=0)

map_widget.set_position(52.2297, 21.0122)

map_widget.set_zoom(6)

# KLIENT MAPA

map_widget_klienci = tkintermapview.TkinterMapView(
    ramka_mapa_klienci,
    width=1000,
    height=500
)

map_widget_klienci.grid(row=0, column=0)

map_widget_klienci.set_position(52.2297, 21.0122)
map_widget_klienci.set_zoom(6)

# PRACOWNIK MAPA

map_widget_pracownicy = tkintermapview.TkinterMapView(
    ramka_mapa_pracownicy,
    width=1000,
    height=500
)
map_widget_pracownicy.grid(row=0, column=0)

map_widget_pracownicy.set_position(52.2297, 21.0122)

map_widget_pracownicy.set_zoom(6)

for biblioteka in biblioteki:
    lista_bibliotek.insert(
        END,
        biblioteka["nazwa"]
    )

    marker = map_widget.set_marker(
        biblioteka["lat"],
        biblioteka["lon"],
        text=biblioteka["nazwa"]
    )

    markers.append(marker)

for klient in klienci:
    lista_klientow.insert(
        END,
        f"{klient['imie']} {klient['nazwisko']}"
    )

    marker = map_widget_klienci.set_marker(
        klient["lat"],
        klient["lon"],
        text=f"{klient['imie']} {klient['nazwisko']}"
    )

    client_markers.append(marker)

for pracownik in pracownicy:
    lista_pracownikow.insert(
        END,
        f"{pracownik['imie']} {pracownik['nazwisko']}"
    )

    marker = map_widget_pracownicy.set_marker(
        pracownik["lat"],
        pracownik["lon"],
        text=f"{pracownik['imie']} {pracownik['nazwisko']}"
    )

    employee_markers.append(marker)

for ksiazka in ksiazki:
    lista_ksiazek.insert(
        END,
        ksiazka["tytul"]
    )


for wypozyczenie in wypozyczenia:

    lista_wypozyczen.insert(
        END,
        f"{wypozyczenie['klient']} -> {wypozyczenie['ksiazka']}"
    )

root.mainloop()
