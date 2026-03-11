#Peso molecular Arginina e Tirosina

nome_do_aminoacido = input("ARGININA ou TIROSINA ? ")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794
if(nome_do_aminoacido == "ARGININA"):
	peso_molecular = (6*C) + (15 * H) + (4 * N) + (2 * O)
	print(round(peso_molecular,2))

else:
	peso_molecular = (C*9) + (H*11) + (N*1) + (O*3)
	print(round(peso_molecular,2))