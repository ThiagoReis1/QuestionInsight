from numpy import*
alunos = array(eval(input("Informe o percentual de aluna frequentado:\n")))
#aux = zeros(size(alunos), dtype = int)
cont = 0
j = 0
for i in range(size(alunos)):
	if (alunos[i]>=70):
		cont = cont + 1
aux = zeros(cont, dtype=int)
for i in range (size(alunos)):
	if(alunos[i]>=70):
		aux[j] = i
		j = j + 1
		
print(cont)
print(aux)