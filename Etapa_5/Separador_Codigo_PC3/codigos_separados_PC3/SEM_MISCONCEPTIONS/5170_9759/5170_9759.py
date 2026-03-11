peso = float(input("Informe o o valor do peso do saco de racao em gramas: "))

quant = float(input("Informe a quantidade diaria de racao: "))

a = peso - (quant * 7)
print(round(a, 3))