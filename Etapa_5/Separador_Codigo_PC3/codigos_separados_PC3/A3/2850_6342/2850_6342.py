from numpy import*

v = array(eval(input('escreva soma: ')))
total = 0
soma = 0

for i in range (size(v)):
	total = total + v[i]
	if total >= 55:
		total = 0
		
print(total)
		
	