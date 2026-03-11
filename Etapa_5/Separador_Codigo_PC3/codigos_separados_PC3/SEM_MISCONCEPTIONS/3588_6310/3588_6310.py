pesos = [2.0, 1.0, 0.5, 0.25]
acertados = eval(input())
total = 10000
for i in acertados:
	total = total*pesos[i-1]
print(round(total,2))
