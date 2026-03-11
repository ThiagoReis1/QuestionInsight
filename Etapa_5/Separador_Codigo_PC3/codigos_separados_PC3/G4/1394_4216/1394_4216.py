qh = int(input("Quantidade de horas: "))

e1 = (50*qh)
e2 =  50*20 + (qh-20)*70


if(qh<=20):
	print(float(round(e1, 2)))
else:
	print(float(round(e2, 2)))