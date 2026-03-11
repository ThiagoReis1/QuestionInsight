idade= int(input(""))
p= float(input(""))

if idade > 0 and idade < 130 and p > 0 and p < 550.0:
	if idade <= 20 and p <= 60:
		print("Grupo de risco: 9")
	elif idade <= 20 and p > 60 and p <= 90:
		print("Grupo de risco: 8")
	elif idade > 90:
		print("Grupo de risco: 7")
	elif idade > 20 and idade <= 50 and p <= 60:
		print("Grupo de risco: 6")
	elif idade > 20 and idade <= 50 and p > 60 and p <= 90:
		print("Grupo de risco: 5")
	elif idade > 20 and idade <= 50 and p > 90:
		print("Grupo de risco: 4")
	elif idade > 50 and p <= 60:
		print("Grupo de risco: 3")
	elif idade > 50 and p > 60 and p <= 90:
		print("Grupo de risco: 2")
	elif idade > 50 and p > 90:
		print("Grupo de risco: 1")
	else:
		print("Dados invalidos")
else: 
	print("Dados invalidos")