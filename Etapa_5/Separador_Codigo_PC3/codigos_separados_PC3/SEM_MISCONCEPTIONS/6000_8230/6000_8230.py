cachos = int(input("informe o numero de cachos: "))

if (cachos < 3):
	total = (cachos*5)
	print(round(total, 2))
	
else:
	total = (cachos*4.25)
	print(round(total, 2))