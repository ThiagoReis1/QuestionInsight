from numpy import *
alunos_ap = array(eval(input("alunos aP:")))
cont =0
for i in alunos_ap:
	if i>=70:
		cont +=1
print(cont)
j=0
v=zeros(cont, dtype=int)
for i in range(size(alunos_ap)):
	if alunos_ap[i]>=70:
		v[j]=i
		j+=1
print(v)