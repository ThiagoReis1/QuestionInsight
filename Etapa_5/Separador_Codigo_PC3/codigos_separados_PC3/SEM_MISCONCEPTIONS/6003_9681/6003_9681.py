compradas = int(input("Numero de cenouras compradas: "))
if compradas >= 5:
	total = compradas * 0.90
	print(round(total,2))
else:
	total = compradas * 1.20
	print(round(total,2))