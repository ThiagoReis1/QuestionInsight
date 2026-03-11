x = float(input("Digite o numero: "))
k = int(input("Digite o numero: "))
soma=0
i=0
while(i<k):
	soma = soma + (x**(1+i))/(1+i) * (-1)**i
	i = i + 1 
print(round(soma,10))