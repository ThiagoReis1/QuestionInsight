v = float(input("Valor do premio: "))
m = float(input("Saque mensal: "))
j = float(input("Taxa de juros: "))/100
p = v
t = 0
if (v > 0) and (m > 0) and (j > 0):
	while (p < (v + 0.2*v)):
		p = p + p*j
		p = round(p - m, 2)
		t = t + 1
	print(t)
else:
	print("Dados incorretos")