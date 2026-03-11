x=float(input('x:'))
k=int(input('k:'))
i=1
soma=0
while i<=k:
	soma=soma+(i/(2*i*(x)))
	i=i+1
print(round(soma,10))

