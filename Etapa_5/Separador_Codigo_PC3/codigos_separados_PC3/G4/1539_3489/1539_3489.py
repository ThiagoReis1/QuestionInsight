x = float(input("digite x: "))
k = int(input("digite k: "))

soma = 0
i = 0
eq = 0
while (i < k) :
	eq = (((-1)** soma) * (x**i)) + eq
	soma = soma + 1
	i = i + 1
print(round(eq,7))