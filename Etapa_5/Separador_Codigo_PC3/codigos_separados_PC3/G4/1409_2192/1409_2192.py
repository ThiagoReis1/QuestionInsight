ataque = input()
d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

if(ataque == "espada"):
	dano = int((d1 + 6) + (d2 + 6) + (d3 + 6) + (d4 + 6))
	print(dano)
	
else:
	dano = int((d1 + d2 + d3)*d4)
	print(dano)