from numpy import *
temp=array(eval(input("Informe as temperaturas:")))
i=0
s=0

while(i<size(temp)):
	if(temp[i]<=50):
		i=i+1
	else:
		i=i+1
		s=s+1

temp2=array(zeros(size(temp)-s, dtype=float))
i=0
z=0

while(i < size(temp)):
	if(temp[i]>50):
		i=i+1
	else:
		temp2[z]=temp[i]
		i=i+1
		z=z+1
		
print(temp2)


		


		