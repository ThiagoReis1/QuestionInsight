x=float(input("insira um valor: "))
k=int(input("numero de termos:"))
i=1
soma=0
while(i<=k):
	soma=soma+x/(2*i)
	i=i+1
print(round(soma,8))