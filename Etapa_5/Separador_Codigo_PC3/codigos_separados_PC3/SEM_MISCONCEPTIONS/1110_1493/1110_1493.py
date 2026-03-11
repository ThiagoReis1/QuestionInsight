#Universidade Federal do Amazonas
#Avaliacao Parcial 03
#Michael Evangelista da Cruz
#21/07/2016

x = int(input("Qual o prato?: "))
y = int(input("Qual a sobremesa?: "))
z = int(input("Qual a bebida?: "))

print("Entradas: ", x, ",", y, ",", z)

if ((x>= 1 and x<=4) and (y>= 1 and y<=4) and (z>= 1 and z<=4)):
		
	if x == "1":
		Cal_x = 180
	elif x == "2":
		Cal_x = 230
	elif x == "3":
		Cal_x = 250
	elif x == "4":
		Cal_x = 350
		
	Cal_x = a
	
	if y == "1":
		Cal_y = 75
	elif y == "2":
		Cal_y = 110
	elif y == "3":
		Cal_y = 170
	elif y == "4":
		Cal_y = 200
		
	Cal_y = b
			
	elif z == "1":
		Cal_z = 20
	elif z == "2":
		Cal_z = 70
	elif z == "3":
		Cal_z = 100
	elif z == "4":
		Cal_z = 65
	
	Cal_z = c
	
	
	w = a + b +  c
	
	print ("Calorias: ", w, "cal")

else: 
	print("Dados invalidos")