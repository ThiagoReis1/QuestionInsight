peso = float(input("peso da racao em gramas: "))
quantidade = float(input("quantidade diaria de racao em grama: "))
quantidade_atual = float(peso - quantidade * 7)
print(round(quantidade_atual, 4))