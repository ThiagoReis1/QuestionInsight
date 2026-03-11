from numpy import*

t=array(eval(input("lista das turmas: ")))

n=0
for i in range(size(t)):
	if t[i]%5==0:
		n=n+1
print (n)

v=zeros(n, dtype=int)
j=0
for i in range(size(t)):
	if t[i]%5==0:
		v[j]=i
		j=j+1
print (v)