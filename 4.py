numbers = []
while(True):
    start = int(input("Wybierz opcję: \n1. Wprowadzenie liczby\n2. Usunięcie liczby\n3. Wyjście\n"))


    if start == 1:
        num = int(input("Podaj liczbę: "))
        numbers.append(num)
    elif start == 2:
        choice = int(input("Po czym chcesz usunąc liczbę? :\n1. Wartość\n2. Indeks: \n"))
        if choice == 1:
            num = int(input("Podaj liczbę do usunięcia: "))
            numbers.remove(num)
        elif choice == 2:
            ind = int(input("Podaj indeks do usunięcia: "))
            numbers.pop(ind)
    elif start == 3:
        break
    else:
        print("Zły wybór, spróbuj ponownie")

    for ind,val in enumerate(numbers):
        print(f"Indeks: {ind}, Wartość: {val}")
    numbers.reverse()
    print(numbers)
    numbers.sort()
    print(numbers)




