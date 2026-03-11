# Opções de armas para usar (katana ou sabre):
arma = input("Qual arma usar? ")

# Destreza do personagem:
d = int(input("Qual o valor da destreza do personagem? "))

# Os valores sorteados nos dados de dez faces (D1 e D2):
d1 = int(input("Qual o valor do dado 1? "))
d2 = int(input("Qual o valor do dado 2? "))

# Soma das faces sorteadas:
s = d1 + d2

# Dano do golpe da katana:
katana = (2 * s) + d

# Dano do golpe do sabre:
sabre = s + (2 * d)

if (arma == katana):
	print(katana)
else:
	print(sabre)


	
