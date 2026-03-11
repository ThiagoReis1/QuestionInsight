tipoataq = input("Tipo de ataque: ")
nrodadas = int(input("Numero de rodadas: "))
d1 = int(input("d1: "))
d2 = int(input("d2: "))
N = d1+d2
if (tipoataq == "constricao"):
	dano = (N + 1)* nrodadas
else:
	dano = d1 * d2
print(dano)