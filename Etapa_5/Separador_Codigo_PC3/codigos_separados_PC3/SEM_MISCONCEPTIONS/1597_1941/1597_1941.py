from numpy import*
#mais que 80 reais = desconto de 5 reais na compra total

v = array(eval(input(""))) #valor de custo dos itens
y = sum(v)

i = -1
while(v[i]<80):
	i = i + 1
	y = y
while(i<size(v)):
	if(v[i]>80):
	i = i + 1
	y = y - 5

	print(round(y, 2))
