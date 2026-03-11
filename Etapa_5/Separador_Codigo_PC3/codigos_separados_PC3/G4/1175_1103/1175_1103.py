from math import*
num=int(input())
i=1
soma=0
while i<=num :
	soma=soma+((sqrt(i)*(-1)**i)/(6+(2*i+1)))
	i=i+1
print(round(soma,5))	