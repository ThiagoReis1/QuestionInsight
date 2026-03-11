val = float(input("comissao: "))

if val <= 1000.00:
	pagar = val * 0.05
else:
	pagar = (1000.00 * 0.05) + ((val - 1000.00) * 0.1)
print(round(pagar,2))