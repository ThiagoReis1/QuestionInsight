ataque = input()
dado1 = int(input())
dado2 = int(input())

if(ataque == "grito"):
	vida = 6 + dado1 + dado2
	print(vida)
else:
	vida = (dado1 + dado2)*(dado1 + dado2)
	print(vida)
	