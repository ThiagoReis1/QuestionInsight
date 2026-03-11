p = float(input("insira o peso do objeto: "))
if (p < 5000):
	y = p*0.05
else:
	y = p*0.04 + 60
print(round(y, 2))
	