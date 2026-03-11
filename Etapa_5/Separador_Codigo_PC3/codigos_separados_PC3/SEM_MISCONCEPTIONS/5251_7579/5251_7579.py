cidade = input(":").lower()
idade = int(input(":"))

'''
if idade > 0 and idade < 150 and (cidade == "porto velho" or cidade =="santarem" or cidade == "belem" or cidade == "tefe" or cidade == "tabatinga") :
	if cidade == "porto velho":
		if idade <= 2:
			t = 0
			
		elif idade >= 3 and idade <= 12:
			t = 500 / 2
			
		elif idade > 65:
			t = 500 - (500 * 0.30)
			
		elif idade > 12 and idade <= 65:
			t = 500
			
		print("passagem: R$ ",round(t,2))
		
	elif cidade == "santarem":
		if idade <= 2:
			t = 0
			
		elif idade >= 3  and idade <= 12:
			t = 370 /2
			
		elif idade > 65:
			t = 370 - (370 * 0.30)
			
		elif idade > 12 and idade <=65:
			t = 370
			
		print("Passagem: R$ ",round(t,2))
		
	elif cidade == "belem":
		if idade <= 2:
			t = 0
			
		elif idade >= 3 and idade <= 12:
			t = 600/2
			
		elif idade > 65:
			t = 600 - (600 * 0.30)
			
		elif idade > 12 and idade <=65:
			t = 600
			
		print("Passagem : R$ ",round(t,2))
		
	elif cidade == "tefe":
		if idade <= 2:
			t = 0.0
			
		elif idade >= 3 and idade <= 12:
			t = 360 /2
			
		elif idade > 65:
			t = 360 - (360 * 0.30)
			
		elif idade >12 and idade <= 65:
			t = 360
			
		print("passagem: R$ ",round(t,2))
		
	elif cidade == "tabatinga":
		if idade <= 2 :
			t = 0
			
		elif idade >= 3 and idade <= 12:
			t = 550/2
			
		elif idade > 65:
			t = 550 - (550 * 0.30)
			
		elif idade > 12 and idade <= 65:
			t = 550
			
		print("Passagem : R$ ",round(t,2))
		
		
else:
	print("Entradas invalidas")
	'''

if cidade == "porto velho":
	x=500
	
elif cidade == "santarem":
	x=370
	
elif cidade == "belem":
	x=600
	
elif cidade == "tefe":
	x=360
	
elif cidade == "tabatinga":
	x = 550
	
else:
	print("Entradas invalidas")

if idade <=2:
	t = x* 0
	print("Passagem: R$",round(t,2))
	
elif idade >=3 and idade <=12:
	t = x/2
	print("Passagem: R$ ",round(t,2))
	
elif idade > 65 and idade <=150:
	t = x - (x * 0.30)
	print("Passagem: R$ ",round(t,2))
	
else:
	print("Entradas invalidas")
