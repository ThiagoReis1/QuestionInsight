peso = float(input("Peso do saco de racao me gramas: "))
quantidade = float(input("Quantidade diaria de racao em gramas: "))

resto = peso - (quantidade * 7)

print(round(resto, 3))