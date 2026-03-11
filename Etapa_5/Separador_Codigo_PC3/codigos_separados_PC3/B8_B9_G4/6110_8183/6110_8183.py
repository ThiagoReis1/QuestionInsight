QC = int(input("Informe a quantidade de combustivel comum: "))

if (QC < 17.5):
	cal1 = QC + 10.5
	print(cal1)

elif (QC >= 17.5 and QC < 35.0):
	cal2 = QC + 14.0
	print(cal2)
	
elif (QC >= 35.0 and QC < 50.0):
	cal3 = QC + 18.6
	print(cal3)
	
elif (QC == 50 or QC > 50):
	cal4 = QC + 24.5
	print(cal4)
	