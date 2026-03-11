horas = float(input())
if(horas >= 0):
	if(horas >= 0 and horas <= 10):
		pagamento = (horas*50) + 500
		print(round(pagamento,2))
	elif(horas > 10 and horas<=20):
		pagamento = (horas*60) + 600
		print(round(pagamento,2))
	elif(horas > 20 and horas <= 30):
		pagamento = (horas*70) + 700
		print(round(pagamento,2))
	elif(horas > 30):
		pagamento = (horas*80) + 800
		print(round(pagamento,2))
		