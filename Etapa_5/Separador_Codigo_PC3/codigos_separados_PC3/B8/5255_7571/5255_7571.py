peso= float(input("digite o peso: "))
distancia= float(input("digite a distancia: "))
codigo=int(input("digite o codigo: "))
if(codigo==1):	
	total=(peso*25+distancia*0.10)*(1.0+17.0/100)
	print(round(total,2))
elif(codigo==2):
	total=(peso*25+distancia*0.10)*(1.0+17.5/100)
	print(round(total,2))
elif(codigo==3):
	total=(peso*25+distancia*0.10)*(1.0+18.0/100)
	print(round(total,2))
elif(codigo==4):
	total=(peso*25+distancia*0.10)*(1.0+20/100)
	print(round(total,2))
