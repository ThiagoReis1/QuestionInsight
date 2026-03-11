t= (input("Bolo ou salgado: "))
cr= float(input("quantidade de fatias: "))
cc= float(input("quantidade de cappccinos: "))

if(t== "B"):
	x= cr*3.00+cc*5.50
	print(round(x,2))
else:
	z= cr*6+cc*5.50
	print(round(z,2))
		