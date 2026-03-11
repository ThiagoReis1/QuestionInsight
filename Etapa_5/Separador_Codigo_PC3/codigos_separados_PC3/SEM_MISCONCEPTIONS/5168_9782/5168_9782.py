peso_racao = float(input("Peso em gramas: "))
quantidade = float(input("Quantidade diaria: "))

rest = peso_racao - quantidade * 7

print(round(rest, 4))