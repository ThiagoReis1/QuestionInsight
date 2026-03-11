ataque = input("Qual o tipo de ataque? ")
baforadas = int(input("Qual a quantidade de baforadas? "))


Dano1 = baforadas * 40

Dano2 = baforadas * 150

if ("maritimo" == ataque.lower()):
	print("Viserion")
	print(Dano1)
else:
	print("Dragon")
	print(Dano2)
	
	