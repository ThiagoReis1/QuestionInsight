from numpy import*

tapa = array(eval(input()))

i = 0
valor = 100

while(i < size(tapa)):
	if(tapa[i]%2 == 0):
		valor = valor*tapa[i]
	else:
		valor = valor/tapa[i]
	i = i + 1

print(round(valor,2))