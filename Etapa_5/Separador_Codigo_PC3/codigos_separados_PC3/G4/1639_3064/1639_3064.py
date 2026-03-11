from numpy import*

v= array(eval(input("Informe a quantidade de alunos nas turmas: ")))
s=0



for i in range(size(v)):
	if (v[i]%2==0):
		s=s+1
print(s)		

vi=zeros(s,dtype=int)

j=0

for i in range(size(v)):
	if(v[i]%2==0):
		vi[j]=i
		j=j+1
print(vi)		
		