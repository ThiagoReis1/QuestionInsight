peso = float(input("peso do saco de racao em gramas: "))
quantidade = float(input("quantidade diaria de racao em gramas: "))
print(round( peso - quantidade * 5, 3))