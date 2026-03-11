litros = float(input("Digite a quantidade de litros abastecidos: "))

gasolina = 2.86 * litros
total1 = gasolina + 50
total2 = (34/100) * total1
total = total1 + total2
print(round(total,2))
