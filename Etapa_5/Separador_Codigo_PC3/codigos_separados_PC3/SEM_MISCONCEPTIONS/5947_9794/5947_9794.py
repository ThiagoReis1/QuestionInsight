comida = input("C/E: ")
qce = int(input("insira o valor: "))
qs = int(input("insira o valor: "))

if comida == "C":
	coxinha = 2 * qce
	suco = 6 * qs
	total = coxinha + suco
else:
	esfirra = 4.50 *qce
	suco = 6 *qs
	total =  esfirra + suco
print(round(total, 2))


