def pizzaTime(c,qc,qr):
	total = 0
	if c.upper() == "P":
		total = qc * 4.50
	if c.upper() == "L":
		total = qc * 6
	rf = qr * 3
	total += rf
	print(round(total,2))
	
pizzaTime(input(), int(input()), int(input()))