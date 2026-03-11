s = float(input("salario atual: "))

if (s >=0):
	if (s <= 800):
		 a = s + s*0.50
	elif (s <= 1000 and s > 800):
		a = s + s * 0.40
	elif ( s <= 1200 and s > 1000):
		a = s+s*0.30
	elif (s <= 1400 and s> 1200):
		a = s +s *0.20
	elif (s <= 1600 and s> 1200):
		a = s+s*0.10
	else:
		a = s +s*0.05
	print ("Novo salario: R$ ", round(a,2) )
else:
	print ("Dado invalido")