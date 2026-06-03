from controller import *

while True:

    print("\nMENU")

    print("=== BIBLIOTEKI ===")
    print("1 - Dodaj bibliotekę")
    print("2 - Wyświetl biblioteki")
    print("3 - Edytuj bibliotekę")
    print("4 - Usuń bibliotekę")
    print("5 - Pokaż mapę bibliotek")

    print("\n=== KLIENCI ===")
    print("6 - Dodaj klienta")
    print("7 - Wyświetl klientów")
    print("8 - Edytuj klienta")
    print("9 - Usuń klienta")
    print("10 - Pokaż mapę klientów")
    print("11 - Pokaż klientów biblioteki")

    print("\n0 - Wyjście")

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

    elif wybor == "6":
        add_klient()

    elif wybor == "7":
        read_klienci()

    elif wybor == "8":
        update_klient()

    elif wybor == "9":
        delete_klient()

    elif wybor == "10":
        get_mapa_klientow()

    elif wybor == "11":
        read_klienci_biblioteki()

    elif wybor == "0":
        break

