#Nome da arma que devera ser escolhida
a = input("Qual arma voce deseja? (Katana/Sabre): ").lower()

#Valor da destreza do personagem
D = int(input("Insira o valor da destreza: "))

#Valor do primeiro dado d10
d_1 = int(input("Insira o valor do dado 1: "))

#Valor do segundo dado d10
d_2 = int(input("Insira o valor do dado 2: "))

#Valor "S" soma das faces dos dois dados
S = d_1 + d_2

#Condicional para o calculo do dano
if (a == "katana"):
	dano = (2 * S) + D

else:
	dano = S + (2 * D)

print(dano)

