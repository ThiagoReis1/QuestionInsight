extra = float(input("Quantas horas extras trabalhadas? ")) 
trab = float(input("Quantas horas faltou ao servico? "))
h = (extra) - ((2/3)*(trab))
				 
if(extra > 0 and trab > 0):
	if (h > 2400):
		g = 500.0
		print("Entradas:", extra, "horas extras e", trab,"horas de falta")
		print("Gratificacao: R$", g)
	elif(h>1800 and h<=2400):
		g = 400.0
		print("Entradas:", extra, "horas extras e", trab,"horas de falta")
		print("Gratificacao: R$", round(g,2))
	elif (h>1200 and h<=1800):
		g = 300.0
		print("Entradas:", extra, "horas extras e", trab,"horas de falta")
		print("Gratificacao: R$", round(g,2))
	elif(h>600 and h<=1200):
		g = 200.0
		print("Entradas:", extra, "horas extras e", trab,"horas de falta")
		print("Gratificacao: R$", round(g,2))
	elif(h<=600):
		g = 100.0
		print("Entradas:", extra, "horas extras e", trab,"horas de falta")
		print("Gratificacao: R$", round(g,2))	
	else:
		print("Entradas:", extra, "horas extras e", trab,"horas de falta")
		print("Dados invalidos")
else:
	print("Entradas:", extra, "horas extras e", trab,"horas de falta")
	print("Dados invalidos")			 