tipo = input()
rounds = int(input())
d1 = int(input())
d2 = int(input())

if(tipo.lower() == "constricao"):
	print((d1+d2 + 1)*rounds)
	
if(tipo.lower() == "polen"):
	print(d1*d2)