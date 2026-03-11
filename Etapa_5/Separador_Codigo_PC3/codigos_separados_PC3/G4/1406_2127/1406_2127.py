golpe = input("Digite o golpe:")
d1 = int(input("Digite o valor d1:"))
N = int(input("Digite os turnos:"))

if(golpe == "cuspe"):
	dano = (2*d1)*N
	print(dano)
else:
	dano = d1*N
	print(dano)