
x=float(input())
k=int(input())

i=0
soma=0

while(i<k):
	soma=soma + ((-1)**i)*(x**(2*i))
	i=i+1

print(round(soma,8))