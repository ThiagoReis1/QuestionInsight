e = float(input("horas extras: "))
f = float(input("faltas: "))
print("Entradas:",e,"horas extras e",f,"horas de falta")
H = e-(2/3)*f
if(e<0 or f<0):
	print("Dados invalidos")
else:
	if(H>2400):
		x = "Gratificacao: R$ 500.0"
	elif(H>1800 and H<2400):
		x = "Gratificacao: R$ 400.0"
	elif(H>1200 and H<1800):
		x = "Gratificacao: R$ 300.0"
	elif(H>600 and H<1200):
		x = "Gratificacao: R$ 200.0"
	elif(H<600):
		x = "Gratificacao: R$ 100.0"
	print(x)