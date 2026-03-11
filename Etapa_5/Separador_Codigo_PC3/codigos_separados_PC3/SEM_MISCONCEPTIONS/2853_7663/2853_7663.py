from numpy import*
numeros = array(eval(input("numeros: ")))
soma = 0
for i in numeros:
	if i != 10:
		soma = soma + i
	else:
		soma = soma * 10
print(soma)
		
		
