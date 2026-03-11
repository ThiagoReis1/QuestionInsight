# faça seu código aqui
dia = input("Insira o dia da semana(seg, terc, qua, qui, sex, sab, dom): ")
qtdd = int(input("Insira a quantidade de pratos: "))

if dia != "qua":
	total = qtdd * 22
else:
	t = qtdd * 22.0
	total = t - (15/100 * t)
print(round(total, 2))
