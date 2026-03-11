v = float(input("Qual o peso em gramas da encomenda?: "))

if (v < 5000):
	encomenda = v*0.05
else:
	encomenda = v*0.04+60

print(round(encomenda, 2))