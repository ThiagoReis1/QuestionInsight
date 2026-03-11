x = float(input("numero real: "))
k = int(input("numero interio: "))

soma = 0
i = 1
while (i<=k):
	soma = soma + (x/(2*i))
	i = i +1
	
print(round(soma,8))