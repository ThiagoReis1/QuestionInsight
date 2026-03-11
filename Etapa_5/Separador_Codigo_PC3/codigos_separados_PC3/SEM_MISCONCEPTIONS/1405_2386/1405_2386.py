ataque = input("")
dado1 = int(input())
dado2 = int(input())

if(ataque == "toque"):
	print((dado1 + dado2)**2)
else:
	print(6 + dado1 + dado2)