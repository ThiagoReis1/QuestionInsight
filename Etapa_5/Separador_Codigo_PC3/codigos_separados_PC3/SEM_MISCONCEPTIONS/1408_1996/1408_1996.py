# Prova 02 - Ex 02

arma = input("Qual a arma escolhida para o ataque, katana ou sabre? ")
destreza = int(input("Qual a destreza do personagem? "))
dado1 = int(input("Qual o valor do primeiro dado? (1 a 10) "))
dado2 = int(input("Qual o valor do segundo dado? (1 a 10) "))

S = dado1 + dado2

if (arma == "katana"):
	dano = (2 * S) + destreza
	print(dano)
	
else:
	dano = S + (2 * destreza)
	print(dano)