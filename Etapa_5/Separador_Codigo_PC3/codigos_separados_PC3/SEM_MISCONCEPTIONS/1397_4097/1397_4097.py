A = float(input("Digite A: "))

if (A <= 10000):
	custo = 5.00 * A
else:
	custo = 5.00 * A + 4.00 - A 
print(round(custo, 2))
