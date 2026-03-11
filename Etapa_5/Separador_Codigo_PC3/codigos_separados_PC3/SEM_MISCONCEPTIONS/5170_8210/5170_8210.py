peso = float(input("Peso do saco de racao: "))
quant_diaria = float(input("Quantidade diaria: "))
restante = peso - (7*quant_diaria)
print(round(restante, 3))