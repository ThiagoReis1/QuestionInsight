from numpy import*

alunos = array(eval(input("Digite o vetor da quantidade de alunos: ")))

m = 0

for i in range(size(alunos)):
	if alunos[i] % 2 == 0:
		m = m + 1
print(m)
		
cont = zeros(m, dtype = int)
j = 0
k = 0 

for i in range(size(alunos)):
	if alunos[i] % 2 == 0:
		cont[j] = cont[j] + k
		j = j + 1
	k = k + 1	
		
print(cont)