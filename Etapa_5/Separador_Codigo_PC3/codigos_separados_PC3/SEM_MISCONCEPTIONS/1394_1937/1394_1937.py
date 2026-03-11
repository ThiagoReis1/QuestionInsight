horas = float(input())

if(horas <= 20):
	pagamento = 50 * horas

else:
	pagamento = (50*20) + 70*(horas-20)
	
print(round(pagamento,2))