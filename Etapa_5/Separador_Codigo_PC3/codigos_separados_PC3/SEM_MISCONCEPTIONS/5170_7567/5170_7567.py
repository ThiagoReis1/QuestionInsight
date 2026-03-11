peso = float(input("Peso do saco de racao em gramas: "))
quantd = float(input("Quantidade diaria de racao em gramas: "))
quants = peso - (quantd * 7)
print(round(quants, 3))