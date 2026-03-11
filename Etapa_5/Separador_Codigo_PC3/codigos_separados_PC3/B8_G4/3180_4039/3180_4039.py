from numpy import *

vet = array(eval(input()))
a=0
b=0
c=0
d=0
for elemento in vet:
	if(elemento == 1):
		d=d+1
	elif(elemento == 2):
		a=a+1
	elif(elemento == 3):
		c=c+1
	elif(elemento == 4):
		b=b+1
		
v1 = array([d,a,c,b])
print(v1)