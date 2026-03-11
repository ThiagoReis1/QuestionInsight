

tipo=input("tipo de ataque: ")
rod=int(input("numero de rodadas: "))
d1=int(input("valor sorteado dado1: "))
d2=int(input("valor sorteado dado1: "))

if(tipo=="polen"):
	dano = d1 * d2
	print(dano)

else: 
	dd = d1 + d2
	dano2= (dd + 1 ) * rod
	print(dano2)
