am=(input("Digite o nome do aminoacido: ")).upper()
O=15.9994
C=12.011
N=14.00674
H=1.00794
alanina = ((C*3)+(H*7)+(N)+(O*2))
valina = ((C*5)+(H*11)+(N)+(O*2))
tirosina = ((C*9)+(H*11)+(N)+(O*3))
if (am == "ALANINA"):
		print(round(alanina, 2))
elif (am == "VALINA"):
		print(round(valina, 2))
elif(am == "TIROSINA"):
		print(round(tirosina, 2))
else:
	   print("Entrada: X")
		print("Dafo Inval")
			  