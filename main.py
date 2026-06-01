from controller import *

while True:

    print("\nMENU")
    print("1 - Dodaj bibliotekę")
    print("2 - Wyświetl biblioteki")
    print("3 - Edytuj bibliotekę")
    print("4 - Usuń bibliotekę")
    print("0 - Wyjście")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        add_biblioteka()

    if wybor == "2":
        read_biblioteki()

    if wybor == "3":
        update_biblioteka()

    if wybor == "4":
        delete_biblioteka()

    if wybor == "0":
        break