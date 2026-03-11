from numpy import * 
nota = array(eval(input(" Notas: ")))

soma = 0

for i in range(size(nota)):
	if nota[i] != 10:
		soma = soma + nota[i] 
	else:
		soma = soma * 10

print(soma)