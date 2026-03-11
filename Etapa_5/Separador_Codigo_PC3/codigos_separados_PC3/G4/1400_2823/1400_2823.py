a = input("tipo de ataque (constricao/polen):")
b = int(input("numero de rodadas:"))
d1 = int(input("primeiro valor sorteado:"))
d2 = int(input("segundo valor sorteado:"))

if (a == "polen"):
	dano = (d1*d2)
	print(dano)
else:
	dano1 = (d1+d2+1)*b
	print(dano1)

