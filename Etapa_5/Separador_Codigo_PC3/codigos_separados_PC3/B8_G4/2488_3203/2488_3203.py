x = float(input()) #salario

if x>0 :
	if x<=800 :
		y=x*0.5
		s=x+y
		print("Entrada: R$",x)
		print("Novo salario: R$",round(s,2))
	elif 800<x<=1000 :
		y=x*0.4
		s=x+y
		print("Entrada: R$",x)
		print("Novo salario: R$",round(s,2))
	elif 1000<x<=1200 :
		y=x*0.3
		s=x+y
		print("Entrada: R$",x)
		print("Novo salario: R$",round(s,2))
	elif 1200<x<=1400 :
		y=x*0.2
		s=x+y
		print("Entrada: R$",x)
		print("Novo salario: R$",round(s,2))
	elif 1400<x<=1600 :
		y=x*0.1
		s=x+y
		print("Entrada: R$",x)
		print("Novo salario: R$",round(s,2))
	elif x>1600 :
		y=x*0.05
		s=x+y
		print("Entrada: R$",x)
		print("Novo salario: R$",round(s,2))
else:
	print("Entrada: R$",x)
	print("Dado invalido")
		
	
	