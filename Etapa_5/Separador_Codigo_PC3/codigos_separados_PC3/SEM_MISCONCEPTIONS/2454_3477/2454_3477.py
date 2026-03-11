altura= float(input("altura: "))
sexo = input("sexo: ")

if(altura < 1.0) and (altura > 2.5):
	if(sexo.upper()== "M"):
		msg = (altura*72.7)- 58
		print(round(msg,2))
	elif(sexo.upper()== "F"):
		msg = (altura*62.1) - 44.7
		print(round(msg,2))
	else:
		print("codigo invalido de sexo")
else:
	print("altura invalida")

		
		
	
	


	
	
