q = int(input("quantidade de jogos: "))
j1 = float(input("jogo um: "))
v = j1
if(q==2):
	j2 = float(input("jogo dois: "))
	T = j1 + (j2 -(j2 * 0.25))
	print(round(T, 2))
else:
	print(round(v, 2))