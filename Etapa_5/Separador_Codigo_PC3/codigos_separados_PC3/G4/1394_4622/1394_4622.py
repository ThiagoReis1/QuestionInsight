qh = float(input("digite horas: "))

if(qh <= 20):
	sal = 50 * qh
	print(round(sal,2))
else:
	he = qh - 20
	sal = (50 * 20) + (70 * he)
	print(round(sal,2))
	
