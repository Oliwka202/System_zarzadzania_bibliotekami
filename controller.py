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


def update_biblioteka():

    if len(biblioteki) == 0:
        print("Brak bibliotek")
        return

    read_biblioteki()

    numer = int(input("Podaj numer biblioteki do edycji: "))

    if 1 <= numer <= len(biblioteki):

        nowa_nazwa = input("Nowa nazwa: ")
        nowe_miasto = input("Nowe miasto: ")

        biblioteki[numer - 1]["nazwa"] = nowa_nazwa
        biblioteki[numer - 1]["miasto"] = nowe_miasto

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