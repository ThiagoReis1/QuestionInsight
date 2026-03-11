h = int(input("horas :"))



if ( h <= 20  ):
	pagamento = h * 50
else:
	pagamento = (20 * 50) + ((h - 20) * 70)
	
print(float(round(pagamento, 2)))
