mi = float(input("Digite a massa inicial: "))

a = 0

while mi > 0.5:
	mi = mi - mi * 0.10
	a = a + 1
print(a)