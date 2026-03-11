x =  float(input("Valor de x: "))
n = int(input("Valor de n: ")) 
i = 1
soma = 0
while(i <= n):
	soma = soma + i / (2 * i * x)
	i = i + 1
print(round(soma,10))