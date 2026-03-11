n = int(input("numero bacterias: "))
q = int(input("quantidade de horas: "))
h = 0

while(h != q):
	n = int(n + (n * (15/100)))
	h = h + 1
	print(n)