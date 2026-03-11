peso = float(input("Insira o peso em gramas do saco de racao: "))
quantidade = float(input("Insira a quantidade diaria de racao: "))


x = quantidade * 7

y = peso - x

print(round(y,3))

