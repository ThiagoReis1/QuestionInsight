consumo = float(input("consumo de chamadas: "))
total = (consumo * 0.28) + 23
valor = total + (0.31 * total)

print(round(valor, 2))