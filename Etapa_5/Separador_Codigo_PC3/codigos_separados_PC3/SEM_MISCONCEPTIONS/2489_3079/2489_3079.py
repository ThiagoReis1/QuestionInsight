cidade = input()
idade = int(input())

print("Entradas: ", cidade, ",", idade)


if ((idade >= 0) and (cidade == "Porto Velho" or cidade == "Santarem" or cidade == "Belem" or cidade == "Tefe" or cidade == "Tabatinga")):
	if(cidade == "Porto Velho"):
		tarifa = 500.0
		if(idade <= 2):
			total = tarifa - tarifa
			print("Passagem: R$ ", round(total,2))
		elif(3 <= idade <= 12):
			total = tarifa // 2
			print("Passagem: R$ ", round(total,2))
		elif(65<= idade <= 150):
			total = tarifa * 0.7
			print("Passagem: R$ ", round(total,2))
		else:
			total = tarifa
			print("Passagem: R$ ", round(total,2))
	
	elif(cidade == "Santarem"):
		tarifa = 370.0
		if(idade <= 2):
			total = tarifa - tarifa
			print("Passagem: R$ ", round(total,2))
		elif(3 <= idade <= 12):
			total = tarifa // 2
			print("Passagem: R$ ", round(total,2))
		elif(65 <= idade <= 150):
			total = tarifa * 0.7
			print("Passagem: R$ ", round(total,2))
		else:
			total = tarifa
			print("Passagem: R$ ", round(total,2))
	
	elif(cidade == "Belem"):
		tarifa = 600.0
		if(idade <= 2):
			total = tarifa - tarifa
			print("Passagem: R$ ", round(total,2))
		elif(3 <= idade <= 12):
			total = tarifa // 2
			print("Passagem: R$ ", round(total,2))
		elif(65<= idade <= 150):
			total = tarifa * 0.7
			print("Passagem: R$ ", round(total,2))
		else:
			total = tarifa
			print("Passagem: R$ ", round(total,2))
	
	elif(cidade == "Tefe"):
		tarifa = 360.0
		if(idade <= 2):
			total = tarifa - tarifa
			print("Passagem: R$ ", round(total,2))
		elif(3 <= idade <= 12):
			total = tarifa // 2
			print("Passagem: R$ ", round(total,2))
		elif(<= idade , 65):
			total = tarifa * 0.7
			print("Passagem: R$ ", round(total,2))
		else:
			total = tarifa
			print("Passagem: R$ ", round(total,2))
			
	elif(cidade == "Tabatinga"):
		tarifa = 550.0
		if(idade <= 2):
			total = tarifa - tarifa
			print("Passagem: R$ ", round(total,2))
		elif(3 <= idade <= 12):
			total = tarifa // 2
			print("Passagem: R$ ", round(total,2))
		elif(idade >= 65):
			total = tarifa * 0.7
			print("Passagem: R$ ", round(total,2))
		else:
			total = tarifa
			print("Passagem: R$ ", round(total,2))
else:
	print("entradas invalidas")
		