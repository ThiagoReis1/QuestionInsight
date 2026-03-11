x = float(input("numero real: "))
k = int(input("quantidade de termos: "))

i = 1
soma = 0 
while(i <= k):
	soma = soma + i/ (2*i*x)
	i = i + 1
print(round(soma,10))
