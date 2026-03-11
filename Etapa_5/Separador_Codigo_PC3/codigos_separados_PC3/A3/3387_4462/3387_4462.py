unidade = input("digite a letra: ")
medida = float(input("digite o valor: "))
M = 'M'
K = 'K'
if(unidade==M):
	unidade = medida/2.35215
else:
	unidade = 2.35215*medida
print(round(unidade,2))
	
	