from numpy import *
v = array(eval(input("digite: ")))
i = 0
soma = 200
while(i < size(v)):
	if (v[i] == 1):
		soma = soma * 4
	if (v[i] == 2):
		soma = soma * 2
	if (v[i] == 3):
		soma = soma 
	if (v[i] == 4):
		soma = soma / 2
	i = i + 1 
print(round(soma, 2))