from numpy import *

aneis = array(eval(input()))

soma = 0
i = 0
while i < size(aneis):
	if aneis[i] == 1:
		soma += 100
	elif aneis[i] == 2:
		soma += 60
	elif aneis[i] == 3:
		soma += 20
	
	i+=1

print(soma)