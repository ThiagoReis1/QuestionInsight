x=float(input())
k=int(input())

i=1
soma=0
divisor=2

while (i<=k):
	soma=soma+i/(divisor*x)
	divisor=divisor+2
	i=i+1
print(round(soma,10))