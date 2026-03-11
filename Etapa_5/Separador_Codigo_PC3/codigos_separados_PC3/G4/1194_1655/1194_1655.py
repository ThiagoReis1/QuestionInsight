from numpy import*
v=array(eval(input()))
i=0
j=0
while i<size(v):

	if(v[i]<-100):
		j=j+1
	i=i+1	
v1=array(zeros(size(v)-j,dtype=float))
k=0
i=0
while i<size(v):
	if(v[i]>-100):
		v1[k]=v[i]
		k=k+1
	i=i+1
print(v1)	
	