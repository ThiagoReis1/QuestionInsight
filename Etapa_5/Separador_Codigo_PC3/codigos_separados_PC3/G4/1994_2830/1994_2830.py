nome = input().lower()

if((nome == "histidina") or (nome == "leucina") or (nome == "lisina")):
	if(nome == "histidina"):
		p = 6*12.011 + 10*1.0079 + 3*14.00674 + 2*15.9994
		print(round(p,2))
	elif(nome == "leucina"):
		p = 6*12.011 + 13*1.0079 + 1*14.00674 + 2*15.9994
		print(round(p,2))
	else:
		p = 6*12.011 + 15*1.0079 + 2*14.00674 + 2*15.9994
		print(round(p,2))
else:
	print("Entrada:", nome)
	print("Dado Invalido")