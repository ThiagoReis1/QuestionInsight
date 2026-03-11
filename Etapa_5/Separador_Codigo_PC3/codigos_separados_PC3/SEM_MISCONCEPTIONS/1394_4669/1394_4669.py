horas = float(input('Quantidade de horas: '))
if(horas<=20):
	pagamento = horas*50
	print(round(pagamento, 2))
else:
	pagamento = 20*50 + 70*(horas-20)
	print(round(pagamento, 2))
	
	

	