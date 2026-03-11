from numpy import*
v=array(eval(input()))
i=0
j=0
while i<size(v):
	if v[i]<0:
		j+=1
	i+=1
v2=array(zeros(size(v)-j,dtype=float))
k=0
i=0
while i<size(v):
	if v[i]>=0:
		v2[k]=v[i]
		k+=1
	i+=1	
print(v2)

	

	
	