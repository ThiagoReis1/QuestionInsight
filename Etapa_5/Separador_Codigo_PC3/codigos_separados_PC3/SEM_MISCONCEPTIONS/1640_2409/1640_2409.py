from numpy import *
alunos = array(eval(input("quantidade de alunos: ")))
impar = 0
for i in range(size(alunos)):
	if(alunos[i] % 2 != 0):
		impar = impar + 1
print(impar)
vet = zeros(impar, dtype=int)
i = 0
while(i < size(alunos)):
	if(alunos[i] == impar):
		vet[i] = 
		
	