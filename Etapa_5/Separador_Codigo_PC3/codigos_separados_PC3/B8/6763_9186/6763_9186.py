tempo = float(input( "Digite o tempo :"))
tarifa = 5.00
if (tempo < 2):
	total = tarifa + 1.25
	print(round(total, 2))
elif (tempo == 2) :
	total = tarifa + 2.25
	print(round(total, 2))
elif (tempo > 2) :
	total = tarifa + 3.25
	print(round(total, 2))