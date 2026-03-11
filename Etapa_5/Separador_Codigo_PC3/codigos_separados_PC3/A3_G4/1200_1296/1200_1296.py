# Phillip de Sousa
# Av 05, Ex 02
# 11/08/16

from numpy import*

I= array(eval(input("I:")))

i=0
neg=0

while (i < size(I)):
	if I[i] < 0:
		neg = neg + 1
	i=i+1
	
J = array(zeros((size(I))-neg))

j=0
k=0
l=0
y=0
while j < size(I):

	if (I[k]>=0):
		J[l]=I[k]
		l=l+1
	
	k=k+1
	j=j+1
	
print(J)