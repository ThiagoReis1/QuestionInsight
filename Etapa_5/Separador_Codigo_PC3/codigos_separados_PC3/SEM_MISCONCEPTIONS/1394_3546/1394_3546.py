horas = float(input("Horas trabalhadas: "))

if(horas <= 20):
	print( round(horas*50, 2))
else:
	excedente = horas - 20
	pagamento = 20*50 + excedente*70
	print ( round(pagamento, 2))
