nome = input("nome: ")
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794
if (nome.lower() == "aspartato"):
	m = 4 * C + 6 * H + N + 4 * O
	print(round(m, 2))
elif (nome.lower() == "cisteina"):
	m = 3 * C + 7 * H + N + 2 * O + S
	print(round(m, 2))
elif (nome.lower() == "metionina"):
	m = 5 * C + 11 * H + N + 2 * O + S
	print(round(m, 2))
else:
	print("Entrada:", nome)
	print("Dado Invalido")
