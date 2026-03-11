#--------------------------------------------------
#Universidade Federal do Amazonas
#Larisse Gabriele Ramos de Abreu
#Data: 22/11/2016
#
#Objetivo: Katana ou sabre?
#---------------------------------------------------
from math import*
nome_da_arma = input("Nome da arma escolhida para o ataque(katana/sabre): ")
destreza = int(input("Destreza do personagem: "))
dado1 = int(input("Valor sorteado no dado 1: "))
dado2 = int(input("Valor sorteado no dado 2: "))
S = (dado1 + dado2)
if (nome_da_arma == "Katana"):
	dono = (2 * S) + destreza
	print(dano)
elif (nome_da_arma == "sabre"):
	dano = S + (2 * destreza)
	print(dano)