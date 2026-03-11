peso = float(input("Peso da racao: "))
quantidade = float(input("Quantidade diaria: "))

racao = peso - quantidade * 7

print(round(racao,3))