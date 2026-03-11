al2 = 1.65
tc2 = 0.02
al = float(input("Digite sua altura:"))
tc = float(input("Taxa de crescimento:"))
al = 1.42
tc = 0.06
al1 = al
tc1 = tc
contador = 6
while al > tc:
	al = al + tc2
	tc = tc + al2
	print(contador)
	