nome_aminoacido = input()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
peso_glicina = C*2+H*5+N+O*2
peso_serina = C*3+H*7+N+O*3
if(nome_aminoacido == "GLICINA".upper()):
	print(round(peso_glicina,2))
if(nome_aminoacido == "SERINA".upper()):
	print(round(peso_serina,2))