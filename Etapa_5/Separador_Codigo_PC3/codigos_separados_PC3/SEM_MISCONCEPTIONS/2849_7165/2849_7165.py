from numpy import *
notas = array(eval(input("notas: ")))
soma = 0
for x in range(size(notas)):
	soma = soma + notas[x]
	if notas[x] == 0:
			soma = 0
print(soma)