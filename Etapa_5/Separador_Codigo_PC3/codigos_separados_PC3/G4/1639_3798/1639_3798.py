from numpy import*
v=array(eval(input("alunos matriculados ")))
i=0
for elemento in range(size(v)):
	if(v[elemento]%2==0):
		i=i+1
cont=zeros(i,dtype=int)
k=0
for a in range(size(v)):
	if(v[a]%2==0):
		cont[k]=a
		k=k+1
print(i)
print(cont)

