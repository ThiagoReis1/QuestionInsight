ataque = (input("digite o nome do ataque: ")).lower()
d1 = int(input("digite o dado: "))
d2 = int(input("digite o dado: "))

grito = 6 + d1 + d2
toque = ((d1 + d2)**2)

if(ataque == "toque"):
	
	print(int(toque))
	

else:
	print(int(grito))
	