#solucao
peso = float(input("peso da racao: "))
quantidade = float(input("quantidade de racao por dia: "))
d = 4
restara = peso - quantidade * d
print(round(restara, 2))