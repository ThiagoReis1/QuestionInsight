peso = float(input("Peso do saco de racao: "))
quantidade = float(input("Quantidade da racao em gramas: "))
dias = 7

consumido = (peso - (quantidade * dias))

print(round(consumido, 3))