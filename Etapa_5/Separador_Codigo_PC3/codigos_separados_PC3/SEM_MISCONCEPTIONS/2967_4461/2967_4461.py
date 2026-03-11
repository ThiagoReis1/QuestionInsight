altura = float(input("altura: "))
amigo = float(input("alg]tura do amigo: "))
lim = float(input("limite: "))
if(altura > lim or amigo > lim):
	print("Sim") 
else:
	print("Nao")
	
if(altura > amigo):
	print(altura)
else:
	print(amigo)
