from numpy import*

v=array(eval(input( )))


acum=0
i=0

while i<size(v):
	if v[i]<5.0:
		acum=acum+1
	i=i+1
print(acum)

z=zeros(acum,dtype=int)
j=0

while i<size(v):
	if v[i]<5.0:
		z[j]=z[j]+i
		j=j+1
	i=i+1
print(z)
		

	
	