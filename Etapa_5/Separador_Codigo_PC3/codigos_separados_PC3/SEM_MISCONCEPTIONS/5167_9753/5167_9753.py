peso = float(input("peso do saco de racao: "))
quantidade = float(input("quantidade diaria de racao: "))
resto = peso - (quantidade *7)
print(round(resto,3))