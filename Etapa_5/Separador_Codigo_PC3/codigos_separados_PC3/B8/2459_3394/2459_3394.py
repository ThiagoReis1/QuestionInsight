peso=float(input("digite o peso:"))
distancia=float(input("distancia:"))
codigo=float(input("codigo"))
if(codigo==1):
	icms=17.0
elif(codigo==2):
	icms=17.5
elif(codigo==3):
	icms=18
elif(codigo==4):
	icms=20
servico= (((peso*25) + (distancia* 0.10) ) * (1 + (icms/100)))
print(round(servico,2))