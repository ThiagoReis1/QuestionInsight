qi = int(input("Quantidade de pontos de vida:"))
D1 = int(input("D1: "))
D2 = int(input("D2: "))
D3 = int(input("D3: "))

V = (D1 + D2 + D3) * 10
R = qi - V
if R > 0:
	print(R)
	print("VIVO")
else:
	print(0)
	print("MORTO")
	
	