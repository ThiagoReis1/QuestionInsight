# if x % 2 != 0 entao é impar
# quantas contadoras
# para guardar zeros(x,dtype=int)
# guardar o indice 

from numpy import *

qtdalunos = array(eval(input("qtd de alunos matriculados")))
impar = 0
imp = 0
vetor = zeros(impar,dtype=int)
for i in range(size(qtdalunos)):
	if qtdalunos[i] % 2 != 0:
		impar = impar + 1
for i in range(size(qtdalunos)):
	if qtdalunos[i] % 2 != 0:
		impar = impar + 1
		vetor[i] = impar
print(impar)
print(vetor)