from numpy import *

alunos = array(eval(input("Alunos: ")))
cont = 0
for i in range(size(alunos)):
	if alunos[i]%5==0:
		cont+=1
vet = zeros(cont,dtype=int)
j=0
for i in range(size(alunos)):
	if alunos[i]%5==0:
		vet[j]=i
		j+=1	

print(size(vet))		
print(vet)	
	
	
		
	