from numpy import*
a =array(eval(input("Digite:")))
i=0		 
z=0
while(i<size(a)):
	if(a[i]>0):
		z=z+1
	i=i+1
b=array(zeros(z,dtype=float))
j=0
c=0
while(j<size(a)):
	if(a[j]>0):
		b[c]=a[j]	
		c=c+1
	j=j+1
print(b)

			
				