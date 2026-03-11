x = int(input("digito a idade"))
y = float(input("digite o peso "))
if(x >130) or (x < 0) or (y > 550.0) or (y < 0):
		print("Entradas:",x,"anos e",y,"kg")
		print("Dados invalidos")
else:
	
   if( x >= 12) and (y >= 60):
	   z = 1000
   elif( x >= 12) and (y < 60):
	   z = 875
   elif (x < 12) and ( y < 6):
	   z = 75
   elif (x < 12) and ( y > 5) and (y < 10):
	   z = 125
   elif(x < 12) and (y > 9) and (y < 17):
	   z = 250
   elif (x < 12) and ( y > 16) and (y < 25):
	   z = 375
   elif (x < 12) and ( y > 24) and (y < 31):
	   z = 500
   elif (x < 12) and ( y > 30):
	   z = 750
   print("Entradas:", x, "anos e", y, "kg" )
   print("Dosagem:",z,"mg")

