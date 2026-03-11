from numpy import *

a=array(eval(input("entrada: ")))

n=0
while(n >= size(a)):
	if(a[n]>80.0):
		a = a[n]-(a[n]*0.15)
		n = n + 1
	a = a + 1		
b = round(sum(a),2)
print(b)