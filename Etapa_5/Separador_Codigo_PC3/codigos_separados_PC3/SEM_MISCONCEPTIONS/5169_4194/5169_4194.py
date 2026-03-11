peso = float(input("Peso do saco de racao em gramas: "))

quantidade = float(input("Quantidade diaria de racao em gramas: "))

restara = peso - (quantidade * 4)

print(round(restara , 2))