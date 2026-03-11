x = float(input("digite x: "))
k = int(input("digite k: "))

soma = 0
i = 0
sinal = -1
c = 1

while (c < k):
	soma = soma + sinal * (x**c / c)
	soma = -sinal
	c = c + 1
	
print(round(soma, 8))