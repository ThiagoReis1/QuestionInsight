X = input("Digite nome do aminoacido: ").lower()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

if(X == "histidina"): 
	peso = C*6 + H*10 + N*3 + O*2
	print(round(peso, 2))
elif(X == "leucina"):
	peso = C*6 + H*13 + N + O*2
	print(round(peso, 2))
elif(X == "lisina"):
	peso = C*6 + H*15 + N*2 + O*2
	print(round(peso,2))
else:
	print("Entrada:", X)
	print("Dado Invalido")
	
	