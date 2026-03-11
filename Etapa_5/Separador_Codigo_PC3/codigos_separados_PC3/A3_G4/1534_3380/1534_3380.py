from math import*

x = float(input())
k = float(input())

soma=0
n=1
f=1
while (k>0):
	k=k-1
	soma = soma+ (pow(x,n)/(n))
	n=n+2
print(round(soma,7))