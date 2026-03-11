consumo = float(input("Consumo de chamadas em minutos: "))

assin = (consumo * 0.28) + 23
total = assin + (assin * 0.31)

print(round(total, 2))