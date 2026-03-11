ataque = input("constricao ou polen?: ")
rodadas = int(input("quantas rodadas na vinha?: "))
D1 = int(input())
D2 = int(input())
N = D1 + D2
if (ataque == "constricao"):
	ponto = rodadas * (N + 1)
else:
	ponto = (D1 * D2)
print(ponto)