from numpy import *
n = array(eval(input("")))
i = 0
acm = 0
nota = 0
p = 0
while(i < size(n)):
	nota = n[i] * (i + 1)
	acm = acm + nota
	p = p + (i + 1)
	i += 1

print(round(acm / p, 2))




