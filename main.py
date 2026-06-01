from controller import *

while True:

    print("\nMENU")
    print("1 - Dodaj bibliotekę")
    print("2 - Wyświetl biblioteki")
    print("0 - Wyjście")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        add_biblioteka()

    if wybor == "2":
        read_biblioteki()

    if wybor == "0":
        break