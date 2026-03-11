from numpy import *
preco = array(eval(input()))
precos_acima_180 = 0
itens_acima_180 = 0

for i in range(len(preco)):
	if(preco[i] > 180):
		precos_acima_180 = precos_acima_180 + preco[i]
		itens_acima_180 = itens_acima_180 + 1
		
if(itens_acima_180 == 0):
	print(round(0.0, 2))
else:
	media = precos_acima_180 / itens_acima_180
	print(round(media, 2))