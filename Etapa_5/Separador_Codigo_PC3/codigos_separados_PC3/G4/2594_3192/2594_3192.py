from numpy import * 

d = array(eval(input("demandas: ")))

soma = 0

for i in range(size(d)):
	if(d[i] > 100):
		soma = soma + 1
		print(i)
		print(soma)
		
		