x= int(input("idade: "))
y= float(input("peso: "))

print("Entradas:",x,"anos e", y,"kg")
if(x < 0) or (x > 130) or (y < 0.0) or (y > 550.0):
	print("Dados invalidos")
else:
	if(x >= 12) and (y >= 60):
		z=1000
		print("Dosagem:",z,"mg")
	elif(x >= 12) and (y < 60):
		z=875
		print("Dosagem:",z,"mg")
	elif(x < 12) and	(y <= 5):
		z=75
		print("Dosagem:",z,"mg")
	elif(x < 12) and (y > 5) or (y <= 9):
		z=125
		print("Dosagem:",z,"mg")
	elif(x < 12) and (y > 9) or (y <= 16):
		z= 250
		print("Dosagem:",z,"mg")
	elif(x < 12) and (y > 16) or (y <= 24):
		z= 375
		print("Dosagem:",z,"mg")
	elif(x < 12) and (y > 24) or (y <= 30):
		z= 500
		print("Dosagem:",z,"mg")
	elif(x < 12) and (y > 30):
		z= 750
		print("Dosagem:",z,"mg")
	
	