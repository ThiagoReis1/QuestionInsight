ataque = input()
dado1 = int(input())
dado2 = int(input())

if (ataque == 'grito'):
	danos = 6 + (dado1 + dado2)
else :
	danos = (dado1 + dado2) ** 2
	
print(danos)