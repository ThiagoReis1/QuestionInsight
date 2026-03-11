altura_cicero = 1.8
taxa_cicero = 0.01


h = float(input("Altura: "))
tx = float(input("Taxa de crecimento: "))
a = 0
while(h > altura_cicero):
	a = a + 1
	h = h + tx

print(a)
		