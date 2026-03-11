arma = input("arma escolhida: ")
dest = int(input("destreza: "))
d1= int(input("valor do dado 1:"))
d2 = int(input("valor do dado 2:"))
soma = d1 + d2 
if arma == "katana":
	dano = 2*soma + dest
	print(dano)
else: 
	dano = soma + 2*dest
	print(dano)