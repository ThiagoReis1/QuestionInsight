peso = float(input("digite o peso do saco de racao: "))
quantidade = float(input("digite a quantidade diaria de racao: "))
resto = peso - (quantidade * 5)

print(round(resto, 3))
