x =float(input("numero real: "))
n = int(input("quantidade de termos: "))
i = 1
soma = 0
while(i <= n):
	soma = soma + x/(2*i)
	i = i + 1
print(round(soma, 8))
	
