n = int(input("Populacao inicial: "))
ta = float(input("Taxa anual de crescimento: "))
r = int(input("Numero de tracajas roubados: "))

t = ta / 100
i = 0
soma = n
while(n > 0):
	soma = n + (n*t)
	n = soma - (500 + r)
	i = i + 1
print(i)