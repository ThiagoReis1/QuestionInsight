x = float(input("digite um nmr real:"))
k = int(input("digite nmr de termos:"))
i = 0
soma = 0
while(i<k):
	soma = soma + x**(2*i+1)/(2*i + 1)
	i = i + 1
print(round(soma,7))	
