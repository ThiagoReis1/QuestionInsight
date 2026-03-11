from numpy import *
a = array(eval(input("Andares percorridos: ")))
i = 1
p = 0
soma = 0
while(i < size(a)):
	e = a[i] - a[p]
	if(e < 0):
		soma = soma - e
	else:
		soma = soma + e
	i = i + 1
	p = p + 1
m = soma * 3
print(m)