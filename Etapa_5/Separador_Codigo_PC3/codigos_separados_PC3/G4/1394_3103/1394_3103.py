h = float(input("Qual o numero de horas ministradas?: "))
pn = 50 * 20
he = h - 20
if(he > 0):
	pg = pn + he * 70
else:
	pg = 50 * h
print(round(pg,2))	