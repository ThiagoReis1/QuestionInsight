#dicio do cebolinha
from numpy import*

vet = array(eval(input(': ')))
pa = input(': ').upper()
ve = pa.replace('R', 'L')

i = 0


while (ve != vet[i]):
	i = i + 1
	if ve == vet[i]:
		print(i)
	else:
		print('NAO ENCONTRADA')
print(i)


	

	
