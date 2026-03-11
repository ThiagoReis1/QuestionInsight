v = float(input("Digite o valor: "))
q = float(input("Digite a quantidade: "))

if q == 1:
	a = v - ((v * 10)/100)
elif q == 2:
	a = (v * 2) - ((((v * 2) * 30)/100))
elif q >= 3:
	a = (v * q) - ((((v * q) * 40)/100))
print(round(a, 2))