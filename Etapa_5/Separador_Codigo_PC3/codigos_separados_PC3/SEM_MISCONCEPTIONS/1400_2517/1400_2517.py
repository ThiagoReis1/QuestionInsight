nome = input("Danos causados pela Vinha Mortal")
rodadas = float(input("numero de rodadas"))
dado1 = float(input())
dado2 = float(input())
N = dado1 + dado2

if(nome == "constricao"):
   print((N + 1)* rodadas) 
	
else:
	print(dado1 * dado2)
	