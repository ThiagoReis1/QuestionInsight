rpm=float(input(':'))
cont=0
while rpm >= 50:
	print(round(rpm,2))
	rpm -= rpm * 25/100
	cont += 1
