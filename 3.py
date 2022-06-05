from random import randint

numbers = set()
draw = set()
while len(numbers) < 6:
    num = int(input("Podaj kolejnę, wybraną liczbę od 1 do 49: "))
    numbers.add(num)

while len(draw) < 6:
    num = randint(1, 50)
    draw.add(num)

result = list(draw.intersection(numbers))
if len(result) == 0:
    print("Niestety nie trafiłeś żadnej liczby")
elif len(result) == 1:
    print(f"Trafiłeś 1 liczbę! Oto ona: {result}")
else:
    print(f"Trafiłeś {len(result)} liczb! Oto one: {result}")

    



