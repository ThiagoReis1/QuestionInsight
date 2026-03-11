altura_luna = 1.65
taxa_luna = 0.02
a  = float(input())
tx = float(input())
cont = 0
while altura_luna > a:
	cont = cont + 1
	altura_luna = altura_luna + taxa_luna
	a = a + tx
print(cont)