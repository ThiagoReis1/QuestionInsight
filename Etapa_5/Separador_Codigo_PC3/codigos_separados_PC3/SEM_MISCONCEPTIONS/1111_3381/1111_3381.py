extra=float(input())
faltas=float(input())
H=extra-(2/3)*faltas
if((extra>0) and (faltas>0)):
	if(H>2400):
		print("Entradas: ",extra," horas extras e ",faltas," horas de falta")
		print("Gratificacao: R$ 500.00")
	elif(1800<H<=2400):
		print("Entradas: ",extra," horas extras e ",faltas," horas de falta")
		print("Gratificacao: R$ 400.00")
	elif(1200<H<=1800):
		print("Entradas: ",extra," horas extras e ",faltas," horas de falta")
		print("Gratificacao: R$ 300.00")
	elif(600<H<=1200):
		print("Entradas: ",extra," horas extras e ",faltas," horas de falta ")
		print("Gratificacao: R$ 200.00")
	elif(0<H<=600):
		print("Entradas: ",extra," horas extras e ",faltas," horas de falta ")
		print("Gratificacao: R$ 100.00")
	else:
		print("Entradas: ",extra," horas extras e ",faltas," horas de falta ")
		print("Dados invalidos")
else:
	print("Entradas: ",extra," horas extras e ",faltas," horas de falta ")
	print("Dados invalidos")		