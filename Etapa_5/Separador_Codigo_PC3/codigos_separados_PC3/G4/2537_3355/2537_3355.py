e = float(input("Heranca em reais: "))
s = float(input("Saque mensal fixo: "))
j = float(input("Taxa de juros: "))
j = j/100

if ((e > 0) and (s > 0) and (j > 0)):
	t=0
	a = e
	while(a < 1.2*e):
		a = a + a*j
		round(a, 2)
		a = a - s
		t=t+1
	print(t)
else:
	print("Dados incorretos")