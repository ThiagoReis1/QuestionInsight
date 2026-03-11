q1 = int(input("Quantidade de pontos de vida: "))
D1 = int(input("D1: "))
D2 = int(input("D2: "))
D3 = int(input("D3: "))

Y = 200-(D1*10+D2*10+D3*10)
if Y > 0:
	print("VIVO")
else:
	print(0)
	print("MORTO")
	