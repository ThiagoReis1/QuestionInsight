qtd_inicial = int(input())
D1 = int(input())
D2 = int(input())
D3 = int(input())

N = D1 + D2 + D3
perda = 10*N
vida_rest = qtd_inicial - perda

if(vida_rest > 0):
	print(vida_rest)
	print("VIVO")
else:
	print(0)
	print("MORTO")