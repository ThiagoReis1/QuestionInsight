ataque = input(" (constricao/polen) ")
rodadas = int(input())
dado1 = int(input())
dado2 = int(input())




if(ataque == "constricao"):
	danov = (((dado1 + dado2) + 1)*rodadas)
	print(danov)
	
else:
	danop = (dado1 * dado2)
	print(danop)
	

