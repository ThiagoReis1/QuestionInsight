from numpy import *
from numpy.linalg import *

vetor = array(eval(input("Digite as notas dos alunos: ")))


i = 0 				  
numero = 0
rep = 0
				  			  
while (i < size(vetor)):
	if vetor[i] < 5:
		rep = rep + 1
	else:
		numero = numero + 1
	i = i + 1			  
print (numero)

x = 0
y = 0
aprovados = zeros(numero, dtype = int)
while (x < size(aprovados)):
	if vetor[y] >= 5:
		aprovados[x] = y
		x = x + 1
	y = y + 1

print (aprovados)
	