nome = input("leucina ou lisina: ")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
leucina = (O*2) + (N) + (H*13) + (C*6)
lisina= (O*2) + (N*2) + (H* 15) + (C*6)

if(nome.lower() == "leucina"):
   mensagem = (O*2) + (N) + (H*13) + (C*6)
else:
	mensagem = (O*2) + (N*2) + (H*15) + (C*6)
	
print(round(mensagem,2))