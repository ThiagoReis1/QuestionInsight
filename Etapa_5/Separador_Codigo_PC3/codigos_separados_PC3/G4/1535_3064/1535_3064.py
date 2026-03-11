x=float(input("Digite um numero: "))
k=int(input("Informe o numero de termos: "))
soma=0
i=0
d=1
while (i<k)and((x<=-1)or(x<=1)):
	soma=soma+(((-1)**i)*(x**(d))/d)
	i=i+1
	d=d+2
print(round(soma,6))	