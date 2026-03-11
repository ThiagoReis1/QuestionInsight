ataque = str(input("bote um ataque:(espada/cauda)"))
nome1 = "espada"
nome2 = "cauda"
d1 = int(input("Numero do dado :"))
d2 = int(input("Numero do dado :"))
d3 = int(input("Numero do dado :"))
d4 = int(input("Numero do dado :"))
if(ataque==nome1):
	print((d1+6)+(d2+6)+(d3+6)+(d4+6)) 
if(ataque==nome2):
	print((d1+d2+d3)*(d4))