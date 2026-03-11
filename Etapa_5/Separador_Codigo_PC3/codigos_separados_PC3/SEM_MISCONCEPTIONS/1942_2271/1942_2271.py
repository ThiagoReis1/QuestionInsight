aminoacido = input("aminoacido: ")
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
if(aminoacido == "histidina"):
	mensagem = C*6 + H*10 + N*3 + O*2
else: 
	mensagem = C*5 + H*10 + N + O*2
print(round(mensagem, 2))

