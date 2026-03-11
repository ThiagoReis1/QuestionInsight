atk = input("tipo de ataque: ")
v = int(input("valor sorteado: "))
t = int(input("numero de turnos: "))

if (atk.lower() == "cauda"):
	n = v
	n = (n*t)
if (atk.lower() == "cuspe"):
	n = 2*v
	n = (n*t)

print(n)