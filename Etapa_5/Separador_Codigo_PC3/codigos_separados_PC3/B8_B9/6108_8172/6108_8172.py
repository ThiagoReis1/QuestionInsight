gasosa = float(input())

if gasosa > 0:
	if gasosa < 17.5:
		gasosa = gasosa + 1.5
		print(gasosa)
	elif gasosa >= 17.5 and gasosa < 35:
		gasosa = gasosa + 2.3
		print(gasosa)
	elif gasosa >= 35 and gasosa < 50:
		gasosa = gasosa + 3.3
		print(gasosa)
	elif gasosa >= 50:
		gasosa = gasosa + 4.7
		print(gasosa)
else:
	print("entrada sempre maior que 0")