arma = input("Qual a sua arma? Katana ou Sabre?: ")
d = int(input("Digite a destreza do personagem: "))
dado1 = int(input("Qual o valor do dado 1 de dez faces? " ))
dado2 = int(input("Qual o valor do dado 2 de dez faces? " ))
dano = int
s = dado1 + dado2

if(arma == "katana"):
	dano = (2*s) + d
	print(dano)
else:
	dano = s + (2*d)
	print(dano)