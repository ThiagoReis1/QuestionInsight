from numpy import*
alunos= array(eval(input("Quantos alunos? ")))
cont= 0

for i in range(size(alunos)):
	if alunos[i]%5==0:
		cont=cont+1
nv=zeros(cont, dtype=int)
c=0
for j in range(size(alunos)):
	if alunos[j]%5==0:
		nv[c]=j
		c=c+1
print(cont)
print(nv)
