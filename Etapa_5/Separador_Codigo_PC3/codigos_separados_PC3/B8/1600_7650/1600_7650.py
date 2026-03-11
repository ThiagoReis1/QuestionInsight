from numpy import*

v = array(eval(input("itens: ")))

i = 0
valor = 0

while(i < size(v)):
	if(v[i] > 80):
		valor = valor + v[i] * 0.85
	
	elif(v[i] < 80):
		valor = valor + v[i]
	
	i = i + 1
	
print(round(valor , 2))