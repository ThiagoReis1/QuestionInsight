minutos = float(input("Digite o numero de minutos utilizados no mes: "))

consumo = minutos * 0.28 + 23
juros = consumo * 31/100
total = consumo + juros

print(round(total,2))