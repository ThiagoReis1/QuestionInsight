peso = float(input("Qual o peso de racao em gramas?: "))
quantidade = float(input("Qual a quantidade diaria de racao em gramas?: "))


restante = peso - (quantidade*5)

print(round(restante, 2))
