from numpy import*
saq=array(eval(input("Saques realizados:")))
m=size(saq)
a=0
for i in range(m):
	if	(saq[i]<=50):
		a=a+1
v=zeros(a, dtype=int)
j=0
for i in range(m):
	if	(saq[i]<=50):
		v[j]= i
		j=j+1
print(a)
print(v)