x = float(input("Numero real: "))
k = int(input("Numero de termos: "))


p = 0
n = 0
a = 0
m = 1
while (a < k):
	p = p + m*(x**(n))
	n = n + 2
	m = m*-1
	a = a + 1

print(round(p, 8))