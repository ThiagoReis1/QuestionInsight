qcc = int(input("digite a quantidade de combustivel comum: "))

if qcc >0:
	if qcc < 17.5:
		total = qcc + 1.5
		print(round(total, 1))
	elif qcc > 17.5 and qcc < 35.0:
		total = qcc + 2.3
		print(round(total, 1))
	elif qcc > 35.0 and qcc < 50.0:
		total = qcc + 3.3
		print(round(total, 1))
	else:
		total = qcc + 4.7
		print(round(total, 1))