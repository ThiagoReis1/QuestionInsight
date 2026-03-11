Unid=input("Unidade R/G: ")
Ang=float(input("Angulo: "))
if(Unid=="R"):
	Gr=Ang/0.0174533
	print(round(Gr,2))
else:
	R=0.017453*Ang
	print(round(R,2))

