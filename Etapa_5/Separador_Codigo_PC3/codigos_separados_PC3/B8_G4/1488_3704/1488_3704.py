cs = int(input('Consumo de minutos:'))


if cs >= 0 and cs <= 100:
	print (round(cs * 1.20 + 1.0, 2))
elif cs > 100 and cs <= 200:
	print (round(cs * 1.30 + 10.0, 2))
elif cs > 200 and cs <= 300:
	print (round(cs * 1.40 + 20.0, 2))
elif cs > 300:
	print (round(cs*1.5 + 25.0, 2))
