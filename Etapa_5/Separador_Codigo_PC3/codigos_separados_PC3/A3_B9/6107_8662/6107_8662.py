qcc = float(input('Digite o valor: '))

if qcc > 0:
	if qcc < 17.5:
		total = qcc + 1.5
	elif qcc >= 17.5 and qcc < 35:
		total = qcc + 2.3
	elif qcc >= 35 and qcc < 50:
		total = qcc + 3.3
	else:
		total = qcc + 4.7
	print(round(qcc, 1))
