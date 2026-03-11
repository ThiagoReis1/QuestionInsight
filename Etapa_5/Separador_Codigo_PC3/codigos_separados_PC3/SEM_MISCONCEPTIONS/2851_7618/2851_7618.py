from numpy import * 
notas=array(eval(input("notas: ")))

soma=0

for i in range(size(notas)):
	if notas[i] == 99 :
		soma= soma * 2
	else:
		soma = soma + notas[i]
print(soma)