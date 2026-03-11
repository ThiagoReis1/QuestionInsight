life=int(input("pontos de life do personagem:"))
d1=int(input("valor do dado 1:"))
d2=int(input("valor do dado 2:"))
d3=int(input("valor do dado 3:"))
N=d1+d2+d3
turno=10*N
resto=life-(10*N)
if(resto>0):
	print(resto)
	print("vivo".upper())
else:
	print("0")
	print("morto".upper())
	
	