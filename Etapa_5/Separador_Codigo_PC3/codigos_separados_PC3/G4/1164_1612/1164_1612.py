k=float(input("numero:"))

n=1
soma=0
while n<=k:
	
	soma = soma + (-(-1)**n)*n**2/(4+(2*n-1))
	n=n+1
	
print(round(soma,8))	