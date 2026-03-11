m = float(input("Consumo de minutos do cliente:"))
pm = 1.20 * m
mm = (1.40 * m) + 25

if(m <= 100):
	print(round(pm,2))
else:
	print(round(mm,2))