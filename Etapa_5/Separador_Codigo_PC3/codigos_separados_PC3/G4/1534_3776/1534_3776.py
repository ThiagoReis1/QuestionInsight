x=float(input())
k=int(input())
i=0
l=0
soma=0
while l<k:
	soma= soma + (x**(2*i + 1))/(2*i + 1)
	i=i + 1
	l=l + 1
print(round(soma,7))