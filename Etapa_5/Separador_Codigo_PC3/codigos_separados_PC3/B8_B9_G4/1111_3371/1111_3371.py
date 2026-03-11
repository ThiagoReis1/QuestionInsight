E=float(input("numero de horas extras: "))
F=float(input("numero de horas nao trabalhadas: "))
H=E-(2/3)*F
print("Entradas:", round(E, 2), "horas extras e", round(F, 1), "horas de falta")

if(E>0 and F>0):
	if(H<=600):
		x=100.00
	elif(H>600 and H<=1200):
		x=200.00
	elif(H>1200 and H<=1800):
		x=300.00
	elif(H>1800 and H<=2400):
		x=400.00
	elif(H>2400):
		x=500.00
	print("Gratificacao: R$", round(x, 2))
else:
	print("Dados invalidos")
	