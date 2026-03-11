peso = float(input("peso do saco de racao: "))
quantidade = float(input("quantidade diaria de racao em gramas: "))
sn = peso - (quantidade * 7)
print(round(sn, 4))