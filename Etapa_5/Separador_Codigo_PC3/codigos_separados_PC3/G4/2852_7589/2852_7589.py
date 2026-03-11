from numpy import *

v = array(eval(input("Coloque os numeros: ")))

soma = 0

i = 0

while(i < size(v)):
	if (v[i] == 88):
		soma = soma / 2		
	if (v[i] != 88):
		soma = soma + v[i] 
	i = i + 1
	
print(soma)