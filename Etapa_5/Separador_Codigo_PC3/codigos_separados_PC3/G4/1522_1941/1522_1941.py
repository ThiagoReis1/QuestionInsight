q0 = int(input("quantidade inicial de moedas: "))
d = int(input("despesa mensal: "))
m = int(input("moedas coletadas em impostos: "))
r = int(input("moedas roubadas: "))

mes = 0
moeda = q0

if((q0>0)and(d>0)and(m>0)and(r>0)):
	while((moeda > 0)):
		moeda = moeda + m - r - d
		mes = mes + 1

	print(mes)
	