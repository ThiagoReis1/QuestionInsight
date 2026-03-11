m = float(input("massa inicial: "))
a = int(input(" anos: "))


n = 0
while(n < a):
	mp = m * 5/100
	m = m - mp
	print(round(m,2))
	n = n + 1
