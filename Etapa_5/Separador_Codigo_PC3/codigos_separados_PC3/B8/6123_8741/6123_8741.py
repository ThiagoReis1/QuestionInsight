combcomum = int(input("combustivel comum: "))

if combcomum > 0:
	if combcomum < 17.5:
		combtotal = combcomum + 0.8
		print(round(combtotal, 2))
	elif 17.5 <= combcomum < 35.0:
		combtotal = combcomum + 1.3
		print(round(combtotal, 2))
	elif 35.0 <= combcomum < 50:
		combtotal = combcomum + 2.1
		print(round(combtotal, 2))
	elif combcomum >= 50:
		combtotal = combcomum + 3
		print(round(combtotal, 2))
