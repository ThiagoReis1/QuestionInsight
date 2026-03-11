T = float(input("tempo de permanencia em horas: "))

if (T < 2):
	Taxa = 1.25 + 5.00
	print(round(Taxa, 2))
elif (T == 2):
	Taxa = 2.25 + 5.00
	print(round(Taxa, 2))
elif (T > 2):
	Taxa = 3.25 + 5.00
	print(round(Taxa, 2))