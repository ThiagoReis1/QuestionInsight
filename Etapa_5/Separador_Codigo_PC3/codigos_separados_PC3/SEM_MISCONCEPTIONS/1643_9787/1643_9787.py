from numpy import*

alunos = array(eval(input("")))
contador = 0

for i in range(size(alunos)):
	if alunos[i] >= 5:
		contador +=1

ind = zeros(contador, dtype = int)
print(contador)
l = 0
for i in range(size(alunos)):
	if alunos[i] >= 5:
		ind[l] = i
		l = l +1
print(ind)
		
	

		
		
	
