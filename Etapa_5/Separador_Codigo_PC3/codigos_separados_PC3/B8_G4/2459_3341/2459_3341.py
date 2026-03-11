p = int(input("peso: "))
d = int(input("distancia: "))
c = int(input("codigo: "))
if(c==1):
	icms = 17.0
elif(c==2):
	icms = 17.5
elif(c==3):
	icms = 18.0
elif(c==4):
	icms = 20.0
serv = (p * 25 + d * 0.10) * (1.0 + icms/100)
print(round(serv, 2))