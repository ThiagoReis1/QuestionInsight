from numpy import*
v = array(eval(input("Insira os pesos dos levantamentos ")))
i = 0
cont = 0
while (i < size(v)):
	if (v[i] > 307):
		cont = cont + 1
	i = i + 1
print(307)
print (cont)