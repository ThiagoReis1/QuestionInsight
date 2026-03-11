he = float(input("numero de horas extras: "))
hf = float(input("numero de horas falta: "))

print("Entradas:", he,"horas extras e", hf,"horas de falta")

i = he - (2/3 * hf)

if(he > 0 and hf >0):
	if(i > 2400):
		v = 500.0
		print("Gratificacao: R$",round(v, 2))
	elif(1800 < i <= 2400):
		v = 400.0
		print("Gratificacao: R$",round(v, 2))
	elif(1200 < i <= 1800):
		v = 300.0
		print("Gratificacao: R$",round(v, 2))
	elif(600 < i <= 1200):
		v = 200.0
		print("Gratificacao: R$",round(v, 2))
	elif(i <= 600):
		v = 100.0
		print("Gratificacao: R$",round(v, 2))
else:
	print("Dados invalidos")
	
	