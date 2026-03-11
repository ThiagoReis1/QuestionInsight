from numpy import*

alunos = array(eval(input("")))
contador = 0

for i in range(size(alunos)):
	if alunos[i] >= 5:
		contador += 1
		
p = zeros(contador, dtype = int)
print(contador)
m = 0 
for i in range(size(alunos)):
	if alunos[i] >= 5:
	  p[m] = i 
	  m = m + 1 
print(p)
