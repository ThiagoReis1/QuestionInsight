tipo_ataque = input("constricao/polen: ")
rodadas = int(input("quantidade de rodadas: "))
D1 = int(input("digite o valor sorteado: "))
D2 = int(input("digite outro valor sorteado: "))

if(tipo_ataque == "polen"):
	print(D1*D2)
	
else:
	s = (D1+D2 + 1)
	print( s * rodadas)