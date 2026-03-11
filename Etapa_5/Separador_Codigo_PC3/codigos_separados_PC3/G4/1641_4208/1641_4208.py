from numpy import*
turmas=array(eval(input("alunos:")))
t=0
s=0
for i in range(size(turmas)):
	if(turmas[i]%3==0):
		t=t+1
print(t)
v=zeros(t,dtype=int)

for i in range(size(turmas)):
	if(turmas[i]%3==0):
		v[s]=v[s]+i
		s=s+1
print(v)
	

