from numpy import*
compra=array(eval(input("Valor:")))

for i in range (size(compra)):
	if (compra[i])>= 80:
		compra[i]=(compra[i])-((compra[i])*15/100)
print(round(sum(compra),2))
