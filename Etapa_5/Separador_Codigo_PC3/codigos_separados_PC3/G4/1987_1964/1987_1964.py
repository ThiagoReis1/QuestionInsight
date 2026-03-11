A = input("Digite o nome do aminoacido: ").upper()

O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794
if(A=="ALANINA"):
	P=((C*3)+(H*7)+(N)+(O*2))
	print(round(P, 2))
elif(A=="VALINA"):
	P=((C*5)+(H*11)+(N)+(O*2))
	print(round(P, 2))
elif(A=="TIROSINA"):
	P=((C*9)+(H*11)+(N)+(O*3))
	print(round(P, 2))
else:
	P="Dado Invalido"
	print("Entrada: ", A)
	print(P)
	