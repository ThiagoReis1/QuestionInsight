ano =int(input("ano de nascimento:"))
pais = input("pais selecionado:").upper()

im = (2023 - ano)
sobra = (im - 18)
falta = (18 - im)
sobrae = (im -16)
faltae = (16 - im)

if pais == 'B':
	if im >=18:
		print("sim")
		print(sobra)
	elif im <18:
		print ("nao")
		print (falta)
		
	
elif pais == 'E':
	if im >=16:
		print("sim")
		print (sobrae)
	elif im < 16:
		print ("nao")
		print (faltae)