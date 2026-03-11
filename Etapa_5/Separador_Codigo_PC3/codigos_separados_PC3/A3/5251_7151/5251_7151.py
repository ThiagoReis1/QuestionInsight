destino=input("destino")
idade=int(input("idade passageiro"))

print ("Entradas:", destino, ",",idade)

destino=destino.upper()
passagem= 0

if (destino=="BELEM" or destino=="PORTO VELHO" or destino=="SANTAREM" or destino=="TEFE" or destino=="TABATINGA" ) and (idade >0 and idade <150):
	if (destino=="PORTO VELHO"):
		passagem=500
	elif (destino=="SANTAREM"):
		passagem=370
	elif (destino=="BELEM")	:
		passagem=600
	elif (destino=="TEFE"):
		passagem=360
	else:
		passagem=550
		
	if (idade >=0) and (idade <=2):
		passagem=0
	elif (idade >2)and (idade <=12):
		passagem=(passagem*0.5)
	else:
		passagem=(passagem*0.7)
	
	print ("Passagem: R$", round(passagem,2))
else:

	print ("entradas invalidas")
	
		

	
	



	
	