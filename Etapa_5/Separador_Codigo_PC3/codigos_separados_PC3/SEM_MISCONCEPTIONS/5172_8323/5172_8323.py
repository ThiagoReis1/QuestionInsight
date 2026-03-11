peso = float(input("Quantidade em gramas do saco de racao: "))
quantidade = float(input("Quantidade de racao diaria dada ao cachorro: "))
total = peso - (quantidade * 5)

print(round(total, 2))