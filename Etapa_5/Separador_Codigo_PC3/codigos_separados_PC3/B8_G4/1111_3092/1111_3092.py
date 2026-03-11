e=float(input("Horas extras?"))
f=float(input("Horas faltadas?"))

if(f>=0)and(e>=0):
	H=e-(2/3)*f
	if(H<=600):
		g=100.0
		print("Entradas:",e,"horas extras e",f,"horas de falta")
		print("Gratificacao: R$",round(g,2))
	elif(600<H<=1200):
		g=200.0
		print("Entradas:",e,"horas extras e",f,"horas de falta")
		print("Gratificacao: R$",round(g,2))
	elif(1200<H<=1800):
		g=300.0
		print("Entradas:",e,"horas extras e",f,"horas de falta")
		print("Gratificacao: R$",round(g,2))
	elif(1800<H<=2400):
		g=400.0
		print("Entradas:",e,"horas extras e",f,"horas de falta")
		print("Gratificacao: R$",round(g,2))
	elif(2400<H):
		g=500.0
		print("Entradas:",e,"horas extras e",f,"horas de falta")
		print("Gratificacao: R$",round(g,2))
else:
	print("Entradas:",e,"horas extras e",f,"horas de falta")
	print("Dados invalidos")
