from model import biblioteki
import requests
import folium
from bs4 import BeautifulSoup


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