peso = float(input("peso do saco de racao em gramas: "))
quant = float(input("quantidade diaria de racao: "))
quantrest = peso-4*quant
print(round(quantrest, 2))
