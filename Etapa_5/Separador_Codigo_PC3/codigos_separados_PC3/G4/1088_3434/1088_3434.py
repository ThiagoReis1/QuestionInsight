n1 = float(input("nota 01 "))
n2 = float(input("nota 02 "))
n3 = float(input("nota 03 "))
n4 = float(input("nota 04 "))
n5 = float(input("nota 05 "))

med = (n1+n2+n3+n4+n5)/5

if (med >= 7):
	m = "Aprovacao"
else:
	m = "Reprovacao por nota"
print(round(med,2))
print(m)