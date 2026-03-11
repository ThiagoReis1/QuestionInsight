from numpy import*
v=array(eval(input(": ")))
q=0
for i in range (size(v)):
	if v[i]>=70:
		q+=1
z=zeros(q,dtype=int)
j=0
for i in range (size(v)):
	if v[i]>=70:
		z[j]=i
		j+=1
print(q)
print(z)
	