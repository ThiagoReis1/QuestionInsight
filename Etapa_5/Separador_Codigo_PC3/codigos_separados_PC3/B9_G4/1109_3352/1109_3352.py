i= int(float(input("idade:")))
p= float(input("peso:"))

print("Entradas:", i, "anos e", p, "kg")

if(i>=0 and i<=130 and p>=0.0 and p<=550.0):
	if(i>=12):
		if(p>=60):
			d=1000
		else:
			d=875
	elif(i<12 and p<=5):
		d= 75
	elif(i<12 and p>5 and p<=9):
		d= 125
	elif(i<12 and p>9 and p<=16):
		d= 250
	elif(i<12 and p>16 and p<=24):
		d= 375
	elif(i<12 and p>24 and p<=9):
		d=500
	else:
		d=750
	print("Dosagem:",d, "mg")
else:
	print("Dados invalidos")