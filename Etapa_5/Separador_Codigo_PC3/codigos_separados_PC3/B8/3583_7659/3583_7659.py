from numpy import*

compras = array(eval(input("digite o valor das compras: ")))


i = 0
total = 0

while(i<size(compras)):
	if(compras[i] > 50.0):
		a = (compras[i] * 8)/100
		total = total + (compras[i] - a)
	elif(compras[i]<=50.0):
		total = total + compras[i]
	i = i + 1
	
print(round(total, 2))