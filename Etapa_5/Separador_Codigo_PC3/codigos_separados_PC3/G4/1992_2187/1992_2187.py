nome = input("Aminoacido: ")

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794

if(nome.lower() == "glutamina"):
	print(round(5*C + H*8 + N + O*4, 2))
elif(nome.lower() == "histidina"):
	print(round(6*C + H*10 + N*3 + O*2, 2))
elif(nome.lower() == "prolina"):
	print(round(5*C + H*10 + N + O*2, 2))
else:
	print("Entrada: ", nome)
	print("Dado Invalido")