peso = float(input("peso do saco de racao: "))
quantidade = float(input("quantidade diaria de racao em gramas: "))
restante = round(peso - (4 * quantidade), 2)
print(restante)