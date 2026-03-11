peso = float(input("Entre com o peso do saco de racao em gramas = "))
quant = float(input("Entre com a quantidade diaria de racao em gramas = "))

quant_restante = peso - (quant * 7)

print(round(quant_restante, 2))