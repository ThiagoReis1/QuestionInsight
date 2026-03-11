nome = input("nome aminoacido: ")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794
peso = O + C + N + H
ALANINA = C*3 + H*7 + N + O*2
VALINA = C*5 + H*11 + N + O*2
if(nome.upper() == "ALANINA"):
	print(round(ALANINA, 2))
else:
	print(round(VALINA, 2))
	
	