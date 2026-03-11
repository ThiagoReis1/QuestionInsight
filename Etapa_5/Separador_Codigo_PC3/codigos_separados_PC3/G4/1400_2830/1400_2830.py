tipo = input()
rodadas = int(input())
D1 = int(input())
D2 = int(input())

if(tipo.lower() == "constricao"):
	print(rodadas*((D1 + D2)+1))	
	
if(tipo.lower() == "polen"):
	print(D1*D2)
	