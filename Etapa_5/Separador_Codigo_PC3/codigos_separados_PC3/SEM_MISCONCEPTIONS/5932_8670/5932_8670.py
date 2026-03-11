consumo = float(input("O consumo de chamadas no mes: "))

plano = 0.28 * consumo + 23

total = plano * (0.31)

valor_total = plano + total

print(round(valor_total,2))