m = float(input("Informe a massa inicial: "))
n = int(input("Informe os anos: "))
a = 0

while (a < n):
	m = m - m*0.05
	a = a + 1
	print (round(m,2))
	