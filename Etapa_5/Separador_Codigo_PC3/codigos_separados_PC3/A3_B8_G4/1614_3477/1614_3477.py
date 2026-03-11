from numpy import*
prod = input("nome do alimento: ").upper()
qt = array(eval(input("quantidade de gramas: ")))
i = 0 
n = 0
while(i < size(prod)):
	if("banana" == prod[i]):
		soma = soma + (qt[i]*0.97) 
	elif("bife" == prod[i]):
		soma = soma + (qt[i]* 2.95) 
	elif("feijoada" == prod[i]):
		soma = soma + (qt[i]*1.27)
	elif("omelete" == prod[i]):
		soma = soma + (qt[i]*1.04) 
	elif("tomate" == prod[i]):
		soma = soma + (qt[i]*0.2)
	i = i+1 	
print(round(soma,2))		
		
		
	