x= float(input("numero: "))
k= int(input("numero: "))

from math import*

soma=0
n=1
f=1
while (k>0):
	k=k-1
	soma=soma+(pow(-x,n)*f)
	f=f*-1
	n=n+1
print(round(soma,7))