
from model import biblioteki, klienci, pracownicy, ksiazki
import requests
import folium
from bs4 import BeautifulSoup

# BIBLIOTEKI

def add_biblioteka():
    nazwa = input("Podaj nazwę biblioteki: ")
    miasto = input("Podaj miasto: ").title()

    coordinates = get_coordinates(miasto)

    biblioteki.append({
        "nazwa": nazwa,
        "miasto": miasto,
        "lat": coordinates[0],
        "lon": coordinates[1]
    })

    print("Biblioteka została dodana")


def read_biblioteki():

    if len(biblioteki) == 0:
        print("Brak bibliotek")
        return

    for i, biblioteka in enumerate(biblioteki):
        print(f"{i+1}. {biblioteka['nazwa']} - {biblioteka['miasto']}")


def update_biblioteka():

    if len(biblioteki) == 0:
        print("Brak bibliotek")
        return

    read_biblioteki()

    numer = int(input("Podaj numer biblioteki do edycji: "))

    if 1 <= numer <= len(biblioteki):

        nowa_nazwa = input("Nowa nazwa: ")
        nowe_miasto = input("Nowe miasto: ").title()

        biblioteki[numer - 1]["nazwa"] = nowa_nazwa
        biblioteki[numer - 1]["miasto"] = nowe_miasto

        nowe_wspolrzedne = get_coordinates(nowe_miasto)

        biblioteki[numer - 1]["lat"] = nowe_wspolrzedne[0]
        biblioteki[numer - 1]["lon"] = nowe_wspolrzedne[1]

        print("Biblioteka została zaktualizowana")

    else:
        print("Nieprawidłowy numer")


def delete_biblioteka():

    if len(biblioteki) == 0:
        print("Brak bibliotek")
        return

    read_biblioteki()

    numer = int(input("Podaj numer biblioteki do usunięcia: "))

    if 1 <= numer <= len(biblioteki):

        biblioteki.pop(numer - 1)

        print("Biblioteka została usunięta")

    else:
        print("Nieprawidłowy numer")


def get_coordinates(miasto):

    url = f'https://pl.wikipedia.org/wiki/{miasto}'

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)

    response_html = BeautifulSoup(response.text, 'html.parser')

    latitude = float(
        response_html.select('.latitude')[1].text.replace(',', '.')
    )

    longitude = float(
        response_html.select('.longitude')[1].text.replace(',', '.')
    )

    return [latitude, longitude]


def get_mapa():

    m = folium.Map([52, 21], zoom_start=6)

    for biblioteka in biblioteki:

        folium.Marker(
            location=[
                biblioteka['lat'],
                biblioteka['lon']
            ],
            popup=biblioteka['nazwa']
        ).add_to(m)

    m.save("mapa_bibliotek.html")

    print("Mapa została zapisana")

# KLIENCI

def add_klient():

    imie = input("Podaj imię klienta: ").title()
    nazwisko = input("Podaj nazwisko klienta: ").title()

    if len(biblioteki) == 0:
        print("Brak bibliotek")
        return

    print("\nDostępne biblioteki:")

    for i, biblioteka in enumerate(biblioteki):
        print(f"{i+1}. {biblioteka['nazwa']}")

    numer = int(input("Wybierz numer biblioteki: "))

    if 1 <= numer <= len(biblioteki):

        miasto = input("Podaj miasto klienta: ").title()

        coordinates = get_coordinates(miasto)

        klient = {
            "imie": imie,
            "nazwisko": nazwisko,
            "biblioteka": biblioteki[numer - 1]["nazwa"],
            "miasto": miasto,
            "lat": coordinates[0],
            "lon": coordinates[1]
        }

        klienci.append(klient)

        print("Klient został dodany")



def read_klienci():

    if len(klienci) == 0:
        print("Brak klientów")
        return

    for i, klient in enumerate(klienci):
        print(
            f"{i+1}. "
            f"{klient['imie']} "
            f"{klient['nazwisko']} - "
            f"{klient['biblioteka']} - "
            f"{klient['miasto']}"
        )


def update_klient():

    if len(klienci) == 0:
        print("Brak klientów")
        return

    read_klienci()

    numer = int(input("Podaj numer klienta do edycji: "))

    if 1 <= numer <= len(klienci):

        nowe_imie = input("Nowe imię: ").title()
        nowe_nazwisko = input("Nowe nazwisko: ").title()

        print("\nDostępne biblioteki:")

        for i, biblioteka in enumerate(biblioteki):
            print(f"{i+1}. {biblioteka['nazwa']}")

        numer_biblioteki = int(input("Wybierz numer biblioteki: "))

        nowe_miasto = input("Nowe miasto: ").title()

        coordinates = get_coordinates(nowe_miasto)

        if 1 <= numer_biblioteki <= len(biblioteki):

            klienci[numer - 1]["imie"] = nowe_imie
            klienci[numer - 1]["nazwisko"] = nowe_nazwisko
            klienci[numer - 1]["biblioteka"] = biblioteki[numer_biblioteki - 1]["nazwa"]

            klienci[numer - 1]["miasto"] = nowe_miasto
            klienci[numer - 1]["lat"] = coordinates[0]
            klienci[numer - 1]["lon"] = coordinates[1]

            print("Klient został zaktualizowany")


def delete_klient():

    if len(klienci) == 0:
        print("Brak klientów")
        return

    read_klienci()

    numer = int(input("Podaj numer klienta do usunięcia: "))

    if 1 <= numer <= len(klienci):

        klienci.pop(numer - 1)

        print("Klient został usunięty")



def get_mapa_klientow():

    m = folium.Map(location=[52, 21], zoom_start=6)

    for klient in klienci:

        folium.Marker(
            location=[
                klient["lat"],
                klient["lon"]
            ],
            popup=f"{klient['imie']} {klient['nazwisko']}"
        ).add_to(m)

    m.save("mapa_klientow.html")

    print("Mapa klientów została zapisana")

def read_klienci_biblioteki():

    read_biblioteki()

    numer = int(input("Wybierz bibliotekę: "))

    nazwa = biblioteki[numer - 1]["nazwa"]

    print(f"\nKlienci biblioteki {nazwa}:")

    for klient in klienci:
        if klient["biblioteka"] == nazwa:
            print(
                f"{klient['imie']} "
                f"{klient['nazwisko']}"
            )


def add_pracownik():

    imie = input("Podaj imię pracownika: ").title()
    nazwisko = input("Podaj nazwisko pracownika: ").title()

    if len(biblioteki) == 0:
        print("Brak bibliotek")
        return

    print("\nDostępne biblioteki:")

    for i, biblioteka in enumerate(biblioteki):
        print(f"{i+1}. {biblioteka['nazwa']}")

    numer = int(input("Wybierz numer biblioteki: "))

    if 1 <= numer <= len(biblioteki):

        miasto = input("Podaj miasto pracownika: ").title()

        coordinates = get_coordinates(miasto)

        pracownik = {
            "imie": imie,
            "nazwisko": nazwisko,
            "biblioteka": biblioteki[numer - 1]["nazwa"],
            "miasto": miasto,
            "lat": coordinates[0],
            "lon": coordinates[1]
        }

        pracownicy.append(pracownik)

        print("Pracownik został dodany")


def read_pracownicy():

    if len(pracownicy) == 0:
        print("Brak pracowników")
        return

    for i, pracownik in enumerate(pracownicy):

        print(
            f"{i+1}. "
            f"{pracownik['imie']} "
            f"{pracownik['nazwisko']} - "
            f"{pracownik['biblioteka']} - "
            f"{pracownik['miasto']}"
        )


def delete_pracownik():

    if len(pracownicy) == 0:
        print("Brak pracowników")
        return

    read_pracownicy()

    numer = int(input("Podaj numer pracownika do usunięcia: "))

    if 1 <= numer <= len(pracownicy):

        pracownicy.pop(numer - 1)

        print("Pracownik został usunięty")


def update_pracownik():

    if len(pracownicy) == 0:
        print("Brak pracowników")
        return

    read_pracownicy()

    numer = int(input("Podaj numer pracownika do edycji: "))

    if 1 <= numer <= len(pracownicy):

        nowe_imie = input("Nowe imię: ").title()
        nowe_nazwisko = input("Nowe nazwisko: ").title()

        print("\nDostępne biblioteki:")

        for i, biblioteka in enumerate(biblioteki):
            print(f"{i+1}. {biblioteka['nazwa']}")

        numer_biblioteki = int(input("Wybierz numer biblioteki: "))

        nowe_miasto = input("Nowe miasto: ").title()

        coordinates = get_coordinates(nowe_miasto)

        if 1 <= numer_biblioteki <= len(biblioteki):

            pracownicy[numer - 1]["imie"] = nowe_imie
            pracownicy[numer - 1]["nazwisko"] = nowe_nazwisko
            pracownicy[numer - 1]["biblioteka"] = biblioteki[numer_biblioteki - 1]["nazwa"]

            pracownicy[numer - 1]["miasto"] = nowe_miasto
            pracownicy[numer - 1]["lat"] = coordinates[0]
            pracownicy[numer - 1]["lon"] = coordinates[1]

            print("Pracownik został zaktualizowany")


def get_mapa_pracownikow():

    m = folium.Map(location=[52, 21], zoom_start=6)

    for pracownik in pracownicy:

        folium.Marker(
            location=[
                pracownik["lat"],
                pracownik["lon"]
            ],
            popup=f"{pracownik['imie']} {pracownik['nazwisko']}"
        ).add_to(m)

    m.save("mapa_pracownikow.html")

    print("Mapa pracowników została zapisana")




def read_pracownicy_biblioteki():

    if len(biblioteki) == 0:
        print("Brak bibliotek")
        return

    read_biblioteki()

    numer = int(input("Wybierz bibliotekę: "))

    if 1 <= numer <= len(biblioteki):

        nazwa_biblioteki = biblioteki[numer - 1]["nazwa"]

        print(f"\nPracownicy biblioteki {nazwa_biblioteki}:")

        znaleziono = False

        for pracownik in pracownicy:

            if pracownik["biblioteka"] == nazwa_biblioteki:

                print(
                    f"{pracownik['imie']} "
                    f"{pracownik['nazwisko']}"
                )

                znaleziono = True

        if not znaleziono:
            print("Brak pracowników")

# ksiazki

def add_ksiazka():

    tytul = input("Podaj tytuł książki: ").title()
    autor = input("Podaj autora: ").title()

    if len(biblioteki) == 0:
        print("Brak bibliotek")
        return

    print("\nDostępne biblioteki:")

    for i, biblioteka in enumerate(biblioteki):
        print(f"{i+1}. {biblioteka['nazwa']}")

    numer = int(input("Wybierz numer biblioteki: "))

    if 1 <= numer <= len(biblioteki):

        ksiazka = {
            "tytul": tytul,
            "autor": autor,
            "biblioteka": biblioteki[numer - 1]["nazwa"]
        }

        ksiazki.append(ksiazka)

        print("Książka została dodana")

def read_ksiazki():

    if len(ksiazki) == 0:
        print("Brak książek")
        return

    for i, ksiazka in enumerate(ksiazki):

        print(
            f"{i+1}. "
            f"{ksiazka['tytul']} - "
            f"{ksiazka['autor']} - "
            f"{ksiazka['biblioteka']}"
        )


def update_ksiazka():

    if len(ksiazki) == 0:
        print("Brak książek")
        return

    read_ksiazki()

    numer = int(input("Podaj numer książki do edycji: "))

    if 1 <= numer <= len(ksiazki):

        nowy_tytul = input("Nowy tytuł: ").title()
        nowy_autor = input("Nowy autor: ").title()

        print("\nDostępne biblioteki:")

        for i, biblioteka in enumerate(biblioteki):
            print(f"{i+1}. {biblioteka['nazwa']}")

        numer_biblioteki = int(input("Wybierz numer biblioteki: "))

        if 1 <= numer_biblioteki <= len(biblioteki):

            ksiazki[numer - 1]["tytul"] = nowy_tytul
            ksiazki[numer - 1]["autor"] = nowy_autor
            ksiazki[numer - 1]["biblioteka"] = biblioteki[numer_biblioteki - 1]["nazwa"]

            print("Książka została zaktualizowana")

def delete_ksiazka():

    if len(ksiazki) == 0:
        print("Brak książek")
        return

    read_ksiazki()

    numer = int(input("Podaj numer książki do usunięcia: "))

    if 1 <= numer <= len(ksiazki):

        ksiazki.pop(numer - 1)

        print("Książka została usunięta")























