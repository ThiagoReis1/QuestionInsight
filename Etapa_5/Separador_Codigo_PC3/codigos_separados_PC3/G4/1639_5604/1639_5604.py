from numpy import*

v=array(eval(input("alunos: ")))
n=0
j=0

for i in v:
	if i%2==0:
		n=n+1
print(n)

x=zeros(n,dtype=int)
for i in range(size(v)):
	if v[i]%2==0:
		x[j]=i
		j=j+1
			
print(x)