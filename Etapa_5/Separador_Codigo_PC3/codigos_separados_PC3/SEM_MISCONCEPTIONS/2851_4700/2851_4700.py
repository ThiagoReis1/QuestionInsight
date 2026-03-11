from numpy import*

notas = array(eval(input("Digite os valores: ")))

soma = 0
for i in (notas):
	if  i != 99:
		soma = soma + i
	else:
		soma = soma * 2
		
	
print (soma)