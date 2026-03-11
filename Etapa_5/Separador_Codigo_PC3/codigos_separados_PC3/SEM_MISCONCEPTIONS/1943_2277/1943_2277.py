aminoacido = input("digite o nome do aminoacido: ")
O = (15.9994)
C = (12.011)
N = (14.0067)
S = (32.066)
H = (1.00794)

isoleucina = (C*6)+(H*13)+(N)+(O*2)
metionina = (C*5)+(H*11)+(N)+(O*2)+(S)

if(aminoacido == "isoleucina"):
	print(isoleucina)
	
else: 
	print(metionina)