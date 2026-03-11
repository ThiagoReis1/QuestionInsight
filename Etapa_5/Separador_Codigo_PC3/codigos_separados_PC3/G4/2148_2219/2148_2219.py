from numpy import*
tam = array(eval(input("medidas do lado:")))
cont = 0
soma = 0
for i in tam:
	if i >0:
		soma+= i
	if i >= 5:
		cont += 1
		
print(soma)
print(cont)