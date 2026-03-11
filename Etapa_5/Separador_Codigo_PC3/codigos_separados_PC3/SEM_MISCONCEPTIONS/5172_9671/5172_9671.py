peso = float(input("peso do saco de racao em gramas: "))
quant = float(input("quantidade diaria de racao em gramas: "))

final = peso - (quant * 5)

print(round(final, 2))