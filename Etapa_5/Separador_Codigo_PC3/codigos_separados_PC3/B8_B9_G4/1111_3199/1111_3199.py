e = float(input("numero de horas extras: "))
f = float(input("horas faltadas: ")) 
h = e -((2/3)*f)
if (e>0 and f>0):
	if(h>2400):
		g = 500.00
		print("Entradas: ", e, "horas extras e ", f, "horas de falta")
		print("Gratificacao: R$ ", round(g,2))
	elif(h>1800 and h<=2400):
		g = 400.00
		print("Entradas: ", e, "horas extras e ", f, "horas de falta")
		print("Gratificacao: R$ ", round(g,2))
	elif (h>1200 and h<=1800):
		g = 300.00
		print("Entradas: ", e, "horas extras e ", f, "horas de falta")
		print("Gratificacao: R$ ", round(g,2))
	elif (h>600 and h<=1200):
		g = 200.00
		print("Entradas: ", e, "horas extras e ", f, "horas de falta")
		print("Gratificacao: R$ ", round(g,2))
	elif(h<=600):
		g = 100.00
		print("Entradas: ", e, "horas extras e ", f, "horas de falta")
		print("Gratificacao: R$ ", round(g,2))
else:
	print("Entradas: ", e, "horas extras e ", f, "horas de falta")
	print("Dados invalidos")
	
