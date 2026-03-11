p=int(input("Leia o valor do peso: "))
d=int(input("Leia o valor da distancia: "))
cod=int(input("Leia o valor do codigo: "))
if(cod==1):
	icms=17.0
elif(cod==2):
	icms=17.5
elif(cod==3):
	icms=18.0
elif(cod==4):
	icms=20.0
s=(p*25 + d*0.10)*(1.0+icms/100)
print(round(s,2))