gasosa = float(input())

if gasosa > 0:
	if gasosa < 17.5:
		total = gasosa+10.5
		print(round(total,2))
	elif gasosa >= 17.5 and gasosa < 35:
		total = gasosa+14.0
		print(round(total,2))
	elif gasosa >= 35 and gasosa < 50:
		total = gasosa+18.6
		print(round(total,2))
	elif gasosa >= 50.0:
		total = gasosa+ 24.5
		print(round(total,2))