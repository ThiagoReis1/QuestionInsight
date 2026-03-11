h = float(input("Horas trabalhadas:"))

if(h <= 20):
	p = 50 * h
	print (round(p,2))
	
else:
	ex = h - 20
	p = (50 * 20) + (70 * ex)
	print (round(p,2))
	
