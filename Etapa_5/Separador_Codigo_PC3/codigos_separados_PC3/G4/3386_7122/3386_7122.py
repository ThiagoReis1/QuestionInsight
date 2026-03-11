u = input("Unidade de medida R ou G: ")
a = float(input("Angulo: ")) 

if (u.upper()) == "R":
	c =  a / 0.0174533 
	
else:
	c = a * 0.0174533
print(round(c,2))