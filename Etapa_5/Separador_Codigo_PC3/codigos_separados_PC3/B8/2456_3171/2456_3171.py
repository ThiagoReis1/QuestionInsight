payment = float(input("Informe o valor da mensalidade: "))
kid = int(input("Informe o numero de criancas da familia: "))

value_total = payment * kid

if(kid == 1):
	value_to = value_total - ((value_total * 10) / 100)
	print(round(value_to, 2))
elif(kid == 2):
	value_to = value_total  - ((value_total * 30) / 100)
	print(round(value_to, 2))
elif(kid >= 3):
	value_to = value_total  - ((value_total * 40) / 100)
	print(round(value_to, 2))
	