from numpy import*

valor = array(eval(input("Valores: ")))

i = 0

while i < size(valor):
	if valor[i] > 80:
		valor[i] = valor[i] - (valor[i] * (15/100))
	i = i +1	
	
print(round(sum(valor),2))