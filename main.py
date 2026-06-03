from controller import *

while True:

    print("\nMENU")
    print("1 - Dodaj bibliotekę")
    print("2 - Wyświetl biblioteki")
    print("3 - Edytuj bibliotekę")
    print("4 - Usuń bibliotekę")
    print("5 - Pokaż mapę bibliotek")
    print("0 - Wyjście")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        add_biblioteka()

    elif wybor == "2":
        read_biblioteki()

    elif wybor == "3":
        update_biblioteka()

    elif wybor == "4":
        delete_biblioteka()

    elif wybor == "5":
        get_mapa()

    elif wybor == "0":
        break

    else:
        print("Nieprawidłowa opcja")