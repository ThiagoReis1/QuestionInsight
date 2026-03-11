qh = float(input("quantidade de horas: "))

if (qh <= 20):
	p = 50*qh
else:
	p = 50*20 + 70*(qh-20)

print(round(p,2))