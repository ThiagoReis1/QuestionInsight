peso = float(input("Digite o peso do saco de racao em gramas:"))
quantidade = float(input("Digite a quantidade diaria de racao em gramas: "))
restante = peso - (quantidade * 5)
print(round(restante, 2))
