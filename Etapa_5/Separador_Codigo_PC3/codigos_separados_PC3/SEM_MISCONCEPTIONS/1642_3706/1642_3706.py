from numpy import*

alunos = array(eval(input("")))
i = 0
contador=0
while( i != size(alunos)):
	if(alunos[i]%5==0):
		i = i + 1
		contador= contador + 1
	else:
		i = i + 1
n = contador

vetor=zeros(n,dtype=int)
while( i != size(alunos)):
	if(alunos[i]%5==0):
		vetor[i] = vetor[i] + 1
		contador= contador + 1
	else:
		i = i + 1

print(n)
print(vetor)