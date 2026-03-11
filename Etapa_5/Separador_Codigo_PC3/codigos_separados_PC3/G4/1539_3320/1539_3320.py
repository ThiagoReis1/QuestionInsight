x=float(input("numero x: "))
k=int(input("numero de termos: "))
i=0
soma=0
while(i<k):
	soma=soma + (-1)**i * (x**i)
	i=i+1
print(round(soma, 7))
	
	
	