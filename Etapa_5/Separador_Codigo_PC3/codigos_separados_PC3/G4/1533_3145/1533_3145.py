from math import factorial
nr=int(input())
k=int(input())
cont=1
cos=0
pt=0
while cont<=k:
	cos+=nr**pt/factorial(pt)
	cont+=1
	pt+=2
print(round(cos,8))
