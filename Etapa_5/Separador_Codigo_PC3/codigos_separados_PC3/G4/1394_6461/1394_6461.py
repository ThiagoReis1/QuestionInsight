qh = float(input("Quantidade de horas: "))

if qh <= 20:
	vp = qh * 50
	
	
else:
	vp = (qh - 20) * 70 + (20 * 50)
	
print(round(vp, 2))