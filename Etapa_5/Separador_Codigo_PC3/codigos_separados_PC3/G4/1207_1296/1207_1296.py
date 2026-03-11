# Phillip de Sousa
# Av 05, Ex 02
# 11/08/16

from numpy import*

I= array(eval(input("I:")))

R=98.48
i=0
k=0

while (i<size(I)):
   if(R<I[i]):k=k+1
   i=i+1
	
print(R)
print(k)