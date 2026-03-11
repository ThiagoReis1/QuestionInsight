horas = float(input())
if(horas<=20):
	pagamento = horas*50
if(horas>20):
	pagamento = 20*50 +70*(horas-20)
print(round(pagamento,2))