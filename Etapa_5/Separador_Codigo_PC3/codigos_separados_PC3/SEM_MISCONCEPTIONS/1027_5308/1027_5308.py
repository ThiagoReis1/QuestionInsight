consumo = float(input(" quantos kWh consumiu?: "))

consMeroveu = consumo * 0.43

valorfix = consMeroveu + 10

porc = valorfix * 0.25

final = valorfix + porc

print(round(final , 2))