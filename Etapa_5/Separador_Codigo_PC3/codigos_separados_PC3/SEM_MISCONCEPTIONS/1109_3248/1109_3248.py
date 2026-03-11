x = float(input("digite a idade: "))
y = float(input("digite o peso: "))


if(x <=130 and y <=550):
	if(x >= 12 and y >=60):
		z=1000
		print("Entradas:",x,"anos","e",y,"kg")
		print("Dosagem:",z,"mg")	
	elif(y<60):
   		z1 = 875
      print("Entradas:",x,"anos","e",y,"kg")
      print("Dosagem:",z1,"mg")	
	elif(x<12 and y<=5):
	   z2 = 75 
	   print("Entradas:",x,"anos","e",y,"kg")
	   print("Dosagem:",z2,"mg")
	elif(y>5 or y<=9):
		z3= 125 
		print("Entradas:",x,"anos","e",y,"kg")
		print("Dosagem:",z3,"mg")
	elif(y>9 or y<=16):
		z4 = 250 
		print("Entradas:",x,"anos","e",y,"kg")
		print("Dosagem:",z4,"mg")
	elif(y>16 or y<=24):
		z5 = 375 
		print("Entradas:",x,"anos","e",y,"kg")
		print("Dosagem:",z5,"mg")
	elif(y>24 or y<=30):
		z6 = 500 
		print("Entradas:",x,"anos","e",y,"kg")
		print("Dosagem:",z6,"mg")
	elif(y>30):
		z7 = 750 
		print("Entradas:",x,"anos","e",y,"kg")
		print("Dosagem:",z7,"mg")
else:
	print("Entradas:",x,"anos","e",y,"kg")
	print("Dados invalidos")