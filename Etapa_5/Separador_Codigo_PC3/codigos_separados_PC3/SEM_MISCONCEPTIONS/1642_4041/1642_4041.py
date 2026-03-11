from numpy import*
from numpy.linalg import*

qtdalunos = array(eval(input("insira a quantidade de alunos: ")))

cont = 0
j = 0
for i in range(size(qtdalunos)):
	if(qtdalunos[i]%5==0):
		cont = cont + 1

saida = zeros(cont,dtype=int)
for i in range(size(qtdalunos)):
	if(qtdalunos[i]%5==0):
		saida[j] = i
		j = j + 1
		
print(cont)
print(saida)
