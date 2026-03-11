nome = input("Digite o nome do aminoácido: ").upper()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794

if(nome == "ALANINA"):
	print(round(C*3+H*7+N+O*2, 2))
else:
	print(round(C*5+H*11+N+O*2, 2))