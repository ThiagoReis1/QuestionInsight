cabeca = input("Cabeça: ")
D1 = int(input("D1: "))
D2 = int(input("D2: "))
D3 = int(input("D3: "))

if(cabeca == "Aameul"):
	vida = 8 + D1 + D2 + D3
	
else:
	vida = 2 * (D1 + D2 + D3)
	
print(vida)