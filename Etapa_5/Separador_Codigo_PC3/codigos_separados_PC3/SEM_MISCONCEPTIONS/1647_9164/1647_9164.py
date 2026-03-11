from numpy import*
alunos = array(eval(input("Alunos: ")))

cont = 0
for i in range(size(alunos)):
	if alunos [i]>=70:
		cont +=1
print(cont)

vetor = zeros(cont,dtype=int)
j = 0
for i in range(size(alunos)):
	if alunos[i]>=70:
		vetor[j]= i
		j += 1
print(vetor)