n1=float(input("Informe Nota 1:"))
n2=float(input("Informe Nota 2:"))
n3=float(input("Informe Nota 3:"))

medari=(n1+n2+n3)/3
if(medari>=6):
	print(round(medari, 2))
	print("Aprovacao")
else:
	print(round(medari, 2))
	print("Reprovacao")