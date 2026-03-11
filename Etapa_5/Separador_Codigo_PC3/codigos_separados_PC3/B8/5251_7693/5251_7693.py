cidade = input("digite a cidade de destino: ").lower()
idade = int(input("digite a idade do passageiro: "))

if cidade == "porto velho" and idade <= 150:
	if idade >= 65:
		total = 500-500*0.3
		print("Passagem: R$", total)
	elif idade>=3 and idade<=12:
	   total = 500 - 500*0.5
	   print("Passagem: R$", total)
	elif idade <=2:
	   total = 0
	   print("Passagem: R$", total)
if cidade == "santarem" and idade <=150:
	if idade >=65:
		total = 370-370*0.3
		print("Passagem: R$", total)
	elif idade >=3 and idade<=12:
		total = 370 - 370*0.5
		print("Passagem: R$", total)
	elif idade <=2:
		total = 0
		print("Passagem: R$", total)
if cidade == "belem":
	if idade >=65:
		total = 600 - 600*0.3
		print("Passagem: R$", total)
	elif idade >=3 and idade <=12:
		total = 600-600*0.5
		print("Passagem: R$", total)
	elif idade<=2:
		total = 0
		print("Passagem: R$", total)
if cidade == "tefe":
	if idade >=65:
		total = 360 -360*0.3
		print("Passagem: R$", total)
	elif idade >=3 and idade <=12:
		total = 360-360*0.5
		print("Passagem: R$", total)
	elif idade <=2:
		total =0
		print("Passagem: R$", total)
if cidade == "tabatinga":
	if idade >=65:
		total = 550-550*0.3
		print("Passagem: R$", total)
	elif idade >=3 and idade <=12:
		total = 550 - 550*0.5
		print("Passagem: R$", total)
	elif idade <=2:
		total =0
		print("Passagem: R$", total)

	
	
	