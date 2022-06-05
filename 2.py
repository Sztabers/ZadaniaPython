from statistics import mean, median, stdev

przedmioty = {}

while True:
    print(f"Wprowadzone przedmioty: {przedmioty}\n")
    start = int(input("Wybierz opcję: \n1. Wprowadzenie ocen\n2. Obliczenie średniej z ocen\n3. Obliczenie mediany z ocen\n4. Obliczenie odchylenia standradowego z ocen\n5.Wyjście:\n\n"))

    
    if start == 1:
        nazwa = str(input("Podaj nazwę przedmiotu: \n"))
        ocena = int(input("Podaj ocenę z podanego przedmiotu: \n"))
        przedmioty[nazwa] = ocena
    elif start == 2:
        srednia = mean(przedmioty.values())
        print(f"Średnia = {srednia}")
    elif start == 3:
        mediana = median(przedmioty.values())
        print(f"Mediana = {mediana}")
    elif start == 4:
        odchylenie = stdev(przedmioty.values())
        print(f"Odch. Standardowe = {odchylenie}")
    elif start == 5:
        break
    else:
        print("Nieprawidłowy wybór!")




