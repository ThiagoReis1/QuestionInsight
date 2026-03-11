from numpy import*

compra = array(eval(input()))
cont=0
total=0
while (cont != size(compra)):
	if (compra[cont]>80):
		total=total+(compra[cont]-(compra[cont]*0.15))
		cont=cont+1
	else:
		total=total+compra[cont]
		cont=cont+1

print(round(total,2))