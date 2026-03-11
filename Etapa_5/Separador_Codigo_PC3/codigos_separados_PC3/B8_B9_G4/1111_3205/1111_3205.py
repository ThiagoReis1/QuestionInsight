e= float(input())
f= float(input())

h= float(round((e-(2/3)*f),2))

if (h<0):
	print("Entradas:",e,"e",f,("horas de falta"))
	print("Dados invalidos")
	if(h>2400):
		print("Entradas:",e,"horas extras e",f,("horas de falta"))
		print("Gratificacao: R$ 500.00")
	elif(h>1800 and h<=2400):
		print("Entradas:",e,"horas extras e",f,("horas de falta"))
		print("Gratificacao: R$ 400.00")
	elif(h>1200 and h<1800):
		print("Entradas:",e,"horas extras e",f,("horas de falta"))
		print("Gratificacao: R$ 300.00")
	elif(h>600 and h<1200):
		print("Entradas:",e,"horas extras e",f,("horas de falta"))
		print("Gratificacao: R$ 200.00")
	elif(h<=600):
		print("Entradas:",e,"horas extras e",f,("horas de falta"))
		print("Gratificacao: R$ 100.00")

