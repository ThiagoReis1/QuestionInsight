cidade=input("")

if(cidade!="Pentos" and cidade!="Bravos" and cidade!="Lys" and cidade!="Qohor" and cidade!="Norvos" and cidade!="Myr" and cidade!="Tyrosh" and cidade!="Volantis" and cidade!="Lorath"):
	print("Entrada",cidade, "invalida")
	exit()
	
if(cidade=="Pentos"):
	gen="pentoshi"
elif(cidade=="Bravos"):
	gen="bravosiano"
elif(cidade=="Lys"):
	gen="liseno"
elif(cidade=="Qohor"):
	gen="qohorik"
elif(cidade=="Norvos"):
	gen="norvoshi"
elif(cidade=="Myr"):
	gen="myrano"
elif(cidade=="Tyrosh"):
	gen="tyroshi"
elif(cidade=="Volantis"):
	gen="volantino"
elif(cidade=="Lorath"):
	gen="lorathi"
	
print(gen)
	
	
	
	

