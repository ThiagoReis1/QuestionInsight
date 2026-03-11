from numpy import *

n=array(eval(input("numeros:  ")))
for i in range(0, size(n)):
	n[i]=n[i]**2
	
print(n)