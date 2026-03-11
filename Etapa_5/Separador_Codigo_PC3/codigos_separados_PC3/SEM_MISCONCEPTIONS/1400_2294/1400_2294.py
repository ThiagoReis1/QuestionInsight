ataque = input().lower()
rodadas = int(input())
D1 = int(input())
D2 = int(input())
N = D1 * D2
if (ataque == "polen"):
	print(D1 * D2)
else:
	constricao = (N + 1) * rodadas
	print(constricao)