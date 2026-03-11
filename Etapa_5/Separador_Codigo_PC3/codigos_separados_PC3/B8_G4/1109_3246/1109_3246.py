i = int(input())
p = float(input())

print("Entradas: ", i, "anos e", p,"kg")

if(i>=0 and i<=130 and p>= 0.0 and p<=550.0):
	if (i>=12 and p>= 60.0):
		d = 1000
		print("Dosagem: ",d, "mg")
	elif (i>=12 and p<60.0):
		d = 875
		print("Dosagem: ",d, "mg")
	elif (i<12 and p<=5):
		d = 75
		print("Dosagem: ",d, "mg")
	elif (i<12 and p>5 and p<=9):
		d = 125
		print("Dosagem: ",d, "mg")
	elif (i<12 and p>9 and p<=16):
		d = 250
		print("Dosagem: ",d, "mg")
	elif (i<12 and p>16 and p<=24):
		d = 375
		print("Dosagem: ",d, "mg")
	elif (i<12 and p>24 and p<=30):
		d = 500
		print("Dosagem: ",d, "mg")
	elif (i<12 and p>30):
		d = 750
		print("Dosagem: ",d, "mg")
else:
	print("Dados invalidos")