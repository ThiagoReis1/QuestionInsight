x = float(input("Digite um numero: "))
k = int(input("Quantidade de termos: "))
soma = 0 
i = 1
while (i<=k and x>-1 and x<1 and k>0):
	soma = soma + (-1**i)*(x**2*i)
	x = ((1/(soma + (-1**i)*(x**2*i)))**0.5)-1
	i = i + 1
print(round(x,8))