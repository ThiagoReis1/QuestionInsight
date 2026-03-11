cachos = float(input("quantos cachos? "))

if (cachos < 3):
	calc = cachos*5
	print(round(calc,2))
else:
	calc = cachos*4.25
	print(round(calc,2))