from numpy import*

custo = array(eval(input("")))
cont = 0
total = 0
i = 0

while(cont<size(custo)):
	if(custo[cont] > 160):
		total += custo[cont] - 25
		cont += 1
		i += 1
	elif(custo[cont]<=160):
		total += custo[cont]
		cont += 1
print(round(total,2))