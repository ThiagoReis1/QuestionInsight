q =float(input("Quantidade de horas: "))

if (q <= 20 ):
	pagamento=q*50
	print(round(pagamento,2))
else:
	pagamento= q*50+(q-20*)*70
	print(round(pagamento,2))
	
