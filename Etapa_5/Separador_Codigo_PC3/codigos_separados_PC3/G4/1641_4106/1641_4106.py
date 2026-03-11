from numpy import*
v=array(eval(input("Quantidade de alunos matriculados:")))
i=0
x=0
while(i<size(v)):
	if(v[i]%3==0):
		x=x+1
	i=i+1
print(x)
x=zeros(x,dtype=int)
b=0
for i in range(size(v)):
	if(v[i]%3==0):
		x[b]=i
		b=b+1
	
print(x)
	
	
	
