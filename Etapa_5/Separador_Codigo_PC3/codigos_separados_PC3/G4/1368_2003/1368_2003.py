#Trabalho prático 1

#03/11/2016

casca = float(input("Insira a quantidade disponivel de casca de colmeia: "))
alho = float(input("Insira a quantidade disponível de alho: "))
oleo = float(input("Insira a quantidade disponivel de oleo de troll: "))

a = casca // 0.2
b = alho // 0.32
c = oleo // 1.29

antidoto = int(min(a, b, c))

print(antidoto)