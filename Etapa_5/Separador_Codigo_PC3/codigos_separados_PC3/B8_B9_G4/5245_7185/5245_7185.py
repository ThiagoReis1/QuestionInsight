s = float(input())
print ("Entrada: R$", s)

if (s >= 0):
	
	if (s <= 800.00):
		
		a = s * (0.50)
		
	elif (s > 800.00 and s <= 1000.00):
		
		a = s * (0.40)
		
	elif (s > 1000.00 and s <= 1200.00):
		
		a = s * (0.30)
		
	elif (s > 1200.00 and s <= 1400.00):
		
		a = s * (0.20)
		
	elif (s > 1400.00 and s <= 1600.00):
		
		a = s * (0.10)
		
	elif (s > 1600.00):
		
		a = s * (0.05)
		
	
	s = s + a
	print ("Novo salario: R$", round(s, 2))
	
else:
	
	print ("Dado invalido")