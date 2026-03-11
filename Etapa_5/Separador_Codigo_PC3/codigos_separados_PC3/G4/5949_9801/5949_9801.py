Es = input("Qual a escolha? B/C ")
QX = int(input("Quantos? "))
QCap = int(input("Quantos cappuccinos? "))

if Es == "B":
	print(float(QX * 3) + (QCap * 5.5))
else:
	print(float(QX * 6) + (QCap * 5.5))