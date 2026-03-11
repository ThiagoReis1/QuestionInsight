numero1=int(input("informe o prato:"))
numero2=int(input("informe o prato:"))
numero3=int(input("informe o prato:"))
print("Entradas:",numero1,",",numero2,",",numero3)
if(numero1>=1)and(numero1<=4)and(numero2>=1)and(numero2<=4)and(numero3>=1)and(numero3<=4):
	ct=0
	if(numero1==1):
		ct+=180
	elif(numero1==2):
		ct+=230
	elif(numero1==3):
		ct+=250
	else:
	   ct+=350
	if(numero2==1):
		ct+=75
	elif(numero2==2):
		ct+=110
	elif(numero2==3):
		ct+=170
	else:
		ct+=200
	if(numero3==1):
		ct+=20
	elif(numero3==2):
		ct+=70
	elif(numero3==3):
		ct+=100
	else:
		ct+=65
	print("Calorias:",ct,"cal")
else:
	print("Dados invalidos")