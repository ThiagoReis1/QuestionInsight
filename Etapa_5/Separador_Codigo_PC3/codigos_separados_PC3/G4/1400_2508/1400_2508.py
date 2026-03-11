tipo_ataque = input(":")
n_rodadas = int(input(":"))
v1 = int(input(":"))
v2 = int(input(":"))
if(tipo_ataque == "constricao"):
	N = v1 + v2
	p = (N + 1) * n_rodadas
	print(p)
else:
	M = v1 * v2
	print(M)