from model import biblioteki


def add_biblioteka():
    nazwa = input("Podaj nazwę biblioteki: ")
    miasto = input("Podaj miasto: ")

    biblioteki.append({
        "nazwa": nazwa,
        "miasto": miasto
    })

    print("Biblioteka została dodana")


def read_biblioteki():

    if len(biblioteki) == 0:
        print("Brak bibliotek")
        return

    for i, biblioteka in enumerate(biblioteki):
        print(f"{i+1}. {biblioteka['nazwa']} - {biblioteka['miasto']}")