tip1 = input("tipo de ataque:")
rod1 = int(input("rodadas:"))
d1 = int(input("dado :"))
d2 = int(input("dado :"))


if(tip1 == "polen"):
	print(int((d1 * d2)))
if(tip1 == "constricao"):
	n = d1 + d2
	print(int((n + 1) * rod1))