sa = float(input("salario atual: "))

if(sa>0):
	if(0<sa<=800):
		ns = sa * 0.50
		print("Novo salario: R$",(round(ns,2)))
		
	elif(800<sa<=1000):
		ns = sa + (sa * 0.40)
		print("Novo salario: R$",(round(ns,2)))
		
	elif(1000<sa<=1200):
		ns = sa + (sa * 0.30)
		print("Novo salario: R$",(round(ns,2)))
		
	elif(1200<sa<=1400):
		ns = sa + (sa * 0.20)
		print("Novo salario: R$",(round(ns,2)))
		
	elif(1400<sa<=1600):
		ns = sa + (sa * 0.10)
		print("Novo salario: R$",(round(ns,2)))
		
	elif(sa>1600):
		ns = sa + (sa * 0.05)
		print("Novo salario: R$",(round(ns,2)))
		
else:
	print("Dado invalido")
	