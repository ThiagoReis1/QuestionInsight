he=float(input("numero de horas extras: "))
hnt=float(input("numero de horas nao trabalhadas: "))
if((he<0)or(hnt<0)):
	print("Entradas:",he,"horas extras e",hnt,"horas de falta")
	print("Dados invalidos")
else:
	if round((he-2/3*hnt), 2)>2400:
		print("Entradas:",he,"horas extras e",hnt,"horas de falta")
		print("Gratificacao: R$",500.0)
	elif round((he-2/3*hnt),2)>1800 and round((he-2/3*hnt),2)<=2400:
		print("Entradas:",he,"horas extras e",hnt,"horas de falta")
		print("Gratificacao: R$",400.0)
	elif round((he-2/3*hnt),2)>1200 and round((he-2/3*hnt),2)<=1800:
		print("Entradas:",he,"horas extras e",hnt,"horas de falta")
		print("Gratificacao: R$",300.0)
	elif round((he-2/3*hnt),2)>600 and round((he-2/3*hnt),2)<=1200:
		print("Entradas:",he,"horas extras e",hnt,"horas de falta")
		print("Gratificacao: R$",200.0)
	elif round((he-2/3*hnt),2)<=600:
		print("Entradas:",he,"horas extras e",hnt,"horas de falta")
		print("Gratificacao: R$",100.0)