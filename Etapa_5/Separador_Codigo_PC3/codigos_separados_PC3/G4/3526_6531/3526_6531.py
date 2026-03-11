x = float(input("numero real: "))
k = int(input("digite k: "))

soma = 0
i = 0

while(k > 0 and  i < k):
	soma = soma + x ** (2*i + 1) / (2*i + 1)
	i = i + 1
print(round(soma,7))
	
	