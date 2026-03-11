from numpy import*

valor = array(eval(input()))

i = 0
cont = 0

while i < size(valor):
	if valor[i] > 160:
		cont += valor[i]-25
	else:
		cont += valor[i]
	i += 1
print(round(cont,2))
