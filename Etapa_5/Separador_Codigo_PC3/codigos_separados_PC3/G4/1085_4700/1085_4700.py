ap1 = float(input("Nota 1: "))
ap2 = float(input("Nota 2: "))
ap3 = float(input("Nota 3: "))
ap4 = float(input("Nota 4: "))
ap5 = float(input("Nota 5: "))

media = (ap1+ap2+ap3+ap4+ap5)/5

if (media >= 6):
	resultado = "Aprovacao"
else:
	resultado = "Reprovacao"
	
print(round(media,2))
print (resultado)