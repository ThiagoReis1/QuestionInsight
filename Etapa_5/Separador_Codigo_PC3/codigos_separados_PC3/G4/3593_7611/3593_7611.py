from numpy import*

p = 200
i = 0
v = array(eval(input('Insira as faces sorteadas: ')))


while i < size(v):
	
	if v[i] % 2 == 0:
		p = p * 3
	else:
		p = p/2
	i += 1
print(round(p,2))