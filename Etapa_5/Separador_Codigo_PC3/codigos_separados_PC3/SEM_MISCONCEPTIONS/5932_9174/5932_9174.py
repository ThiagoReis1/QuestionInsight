consumo_mes = float(input("consumo mes: "))
total = float((consumo_mes * 0.28) + 23)
valor_total = float(total + 31/100 * total)
print(round(valor_total, 2))