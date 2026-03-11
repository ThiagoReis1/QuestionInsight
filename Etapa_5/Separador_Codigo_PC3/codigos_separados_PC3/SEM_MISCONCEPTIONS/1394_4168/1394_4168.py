h = int(input("horas ministradas:"))
he = h - 20
if (h<=20):
	pagamento = int(h*50) 
	print(round(pagamento,2))
else:
	pagamento = int((20*50) + (70*he))
	print(round(pagamento,2))
 