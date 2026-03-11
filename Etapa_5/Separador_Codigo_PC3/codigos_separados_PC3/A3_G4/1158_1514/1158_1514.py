n = int(input("populacao inicial: "))
ta = float(input("taxa anual de crescimento: "))
r = int(input("numero de tracajas roubados: "))

t = ta/100
i = 0
soma = n
while(n > 0):
	soma = n + (n*t)
	n = soma - (500 + r)
	i = i + 1
print(i)