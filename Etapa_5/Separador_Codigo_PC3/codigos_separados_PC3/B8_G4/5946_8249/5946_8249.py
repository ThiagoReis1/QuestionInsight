lp = (input("lanche ou pizza"))
qlp = int(input())
qr = int(input())


if lp == "L":
	cal1 =  qlp * 6.00
elif lp == "P":
	cal1 = qlp * 4.50

QR = qr * 3.00

total = QR + cal1

print(round(total, 2))

	
	
	
	