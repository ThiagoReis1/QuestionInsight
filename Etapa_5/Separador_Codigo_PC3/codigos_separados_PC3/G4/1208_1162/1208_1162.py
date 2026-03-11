from numpy import *
v = array(eval(input("qual o vetot:")))
i = 0
cont = 0
soma = 0
r = 98.48
print(r)
while(cont < size(v)):
	if(v[i] < r):
		i = i + 1
		soma = soma + 1
	cont = cont + 1
print(soma)