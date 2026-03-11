conta=float(input("digite o valor da conta: "))


if (conta)<=300:
	m=conta+conta*10/100
	print(round(m,2))
else:
	m=conta+conta*6/100
	print(round(m,2))