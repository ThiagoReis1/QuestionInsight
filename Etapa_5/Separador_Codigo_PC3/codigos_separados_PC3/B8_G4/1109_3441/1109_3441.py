#idade
x= int(input("Idade: "))
#peso
y= float(input("Peso: "))
print("Entradas:", x, "anos e", y, "kg")
if y>=0 and y>=550 or x>=0 and x<=130:
	if x>=12 and y>=60:
		print("Dosagem:", 1000, "mg" )
	elif x>=12 and y<60:
		print("Dosagem:", 875, "mg" )
	elif x<12 and y<=5:
		print("Dosagem:", 75, "mg" )
	elif x<12 and y>5 and y<=9 :
		print("Dosagem:", 125, "mg" )
	elif x<12 and y>9 and y<=16 :
		print("Dosagem:", 250, "mg" )
	elif y>16 and y<=24 and x<12:
		print("Dosagem:", 375, "mg" )
	elif x<12 and y>24 and y<=30:
		print("Dosagem:", 500, "mg" )
	elif x<12 and y>30:
		print("Dosagem:", 750, "mg" )
else:
	print("Dados invalidos")
