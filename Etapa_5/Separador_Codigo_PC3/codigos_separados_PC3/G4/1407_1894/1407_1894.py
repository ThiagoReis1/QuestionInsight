qtd = int(input("quantidade inicial de pontos de vida: "))

D1 = int(input("valor do dado 1: "))
D2 = int(input("valor do dado 2: "))
D3 = int(input("valor do dado 3: "))

N = D1 + D2 + D3

perda = 10 * N

if (qtd - perda > 0):
	x = qtd - perda
	print(x)
	print("VIVO")
	
else:
	x = qtd - qtd
	print(x)
	print("MORTO")