cidade = input("qual cidade destino?")
idade = int(input("qual idade do passageiro?"))
print("Entradas:", cidade, ",", idade)
if(cidade.upper() == "PORTO VELHO") and (idade < 150):
	if(idade < 2):
		m = 0.0
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif( 3 < idade < 12):
		p = 500.0 / 2
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif(idade  >= 65 ):
		d = 500 * 0.3
		p = 500 - d
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )
elif(cidade.upper() == "SANTAREM") and (idade < 150):
	if(idade < 2):
		m = 0.0 
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif( 3 < idade < 12):
		p = 370.0 / 2
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif(idade  >= 65 ):
		d = 370 * 0.3
		p = 370 - d
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )
elif(cidade.upper() == "BELEM") and (idade < 150):
	if(idade < 2):
		m = 0.0 
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif( 3 < idade < 12):
		p = 600.0 / 2
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif(idade  >= 65 ):
		d = 600 * 0.3
		p = 600 - d
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )
elif(cidade.upper()== "TEFE") and (idade < 150):
	if(idade < 2):
		m = 0.0 
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif( 3 < idade < 12):
		p = 360.0 / 2
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif(idade  >= 65 ):
		d = 360 * 0.3
		p = 360 - d
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )
elif(cidade.upper() == "TABATINGA") and (idade < 150):
	if(idade < 2):
		m = 0.0 
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif( 3 < idade < 12):
		p = 550.0 / 2
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )
	elif(idade  >= 65 ):
		d = 550 * 0.3
		p = 550 - d
		m = p
		mr = round(m, 2)
		print("Passagem: R$", mr )

else:
	print("entradas invalidas")

