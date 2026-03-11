peso = float(input("Peso do saco: "))
quant_dia = float(input("Quantidade de racao diaria: "))
quant_rest = peso-quant_dia*7
print(round(quant_rest, 2))