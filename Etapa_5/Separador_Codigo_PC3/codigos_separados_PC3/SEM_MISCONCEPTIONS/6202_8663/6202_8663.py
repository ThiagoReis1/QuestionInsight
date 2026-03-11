al = float(input())
tx = float(input())
altura_bia = 1.69
taxa_bia = 0.01
a = 0
while al < altura_bia:
	altura_bia = altura_bia + taxa_bia
	al = al + tx
	a = a + 1
print(a)