from numpy import *

produto=array(eval(input("valor do produto: ")))

i = 0
soma=0

for i in range(size(produto)):
	if produto[i] > 80:
		soma= soma + (produto[i] - 5)
	elif produto[i] <= 80:
		soma=soma + produto[i]
		
print(round(soma,2))