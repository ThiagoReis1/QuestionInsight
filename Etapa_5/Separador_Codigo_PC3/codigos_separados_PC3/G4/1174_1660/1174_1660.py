n = int(input("Qual o valor da seguinte serie? "))
h = 1
x = 1
m = 3
total = 0
qtd = 1
while(n >= qtd):
	s = (((-1 ** h) * (x ** 3)) / (9 + m))
	h = h + 1
	x = x + 1
	m = m + 2
	qtd = qtd + 1
	total = total + s
print(round(total, 8))