arma = input("Arma usada (Katana ou Sabre): ")
d = float(input("Destreza do personagem: "))
d1 = float(input("Valor do dado 1: "))
d2 = float(input("Valor do dado 2: "))
s = d1+d2
if (arma.upper() == "KATANA"):
	x = 2*s+d
	print(x)
else:
	(arma.upper() == "SABRE")
	x = s + 2*d
	print(x)
	
