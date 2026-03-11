cc = float(input("qual a quantidade de combustivel?: "))

if cc < 17.5:
	total = cc + 0.8
	print(round(total, 1))
else:
	if cc >= 17.5 and cc < 35.0:
		total = cc + 1.3
		print(round(total, 1))
	else:
		if cc >= 35.0 and cc < 50.0:
			total = cc + 2.1
			print(round(total, 1))
		else:
			if cc >= 50.0:
				total = cc + 3.0
				print(round(total, 1))	