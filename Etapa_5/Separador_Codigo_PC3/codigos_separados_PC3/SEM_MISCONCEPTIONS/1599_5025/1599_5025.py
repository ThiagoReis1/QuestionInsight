from numpy import*

preco = array(eval(input("Valores dos produtos:")))
i = 0

k = 0
while (i < size(preco)):
	
	if(preco[i] > 80):
		k = k + (preco[i]*0.15)
	i = i + 1

print(round(sum(preco)-k,2))