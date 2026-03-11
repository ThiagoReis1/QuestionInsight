pa = input("Pais: ")
cd = input("Cidade: ")

if((pa.upper() != "ITALIA")or(pa.upper() !="ESPANHA")):
	print("Privincia nao identificada".upper())

else:
	if(pa.upper() == "ITALIA"):
		if((cd.upper() != "ROMA")or(cd.upper() != "FLORENÇA")):
			print("Privincia nao identificada".upper())
		else:
			if(cd.upper() == "ROMA"):
				print("Latina".upper())
			else:
				print("Siena".upper())
	else:
		if((cd.upper() != "FRIGILIANA")or(cd.upper() != "MADRID")):
			print("Privincia nao identificada".upper())
		else:
			if(cd.upper() == "FRIGILIANA"):
				print("Malaga".upper())
			else:
				print("Madrid".upper())

	
	