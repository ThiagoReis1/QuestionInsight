ataque = input()
valor = int(input())
turno = int(input())

cauda = valor * turno
cuspe = (2*valor) * turno

if (ataque == "cauda"):
	print(cauda)
if (ataque == "cuspe"):
	print(cuspe)