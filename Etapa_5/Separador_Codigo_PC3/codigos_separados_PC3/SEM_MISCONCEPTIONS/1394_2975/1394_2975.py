
horas = int(input())
if (horas<=20):
	total  = 50*horas
	print(round(total,2))
else:
	total = 20*50 + ((horas-20)*70)
	print(round(total,2))