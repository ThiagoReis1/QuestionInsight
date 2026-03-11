p = float(input("peso: "))
dist = float(input("distancia: "))
cod = int(input("codigo: "))

ckg = p * 25.00
ckm = dist * 0.1

cod1 = 17/100
cod2 = 17.5/100
cod3 = 18/100
cod4 = 20/100

form = ((p * ckg) + (dist * ckm))

if(cod == 1):
	servico = form * ((1) + cod1)
	print(round(servico, 2))
elif(cod == 2):
	servico = form * ((1) + cod2)
	print(round(servico, 2))
elif(cod == 3):
	servico = form * ((1) + cod3)
	print(round(servico, 2))
elif(cod == 4):
	servico = form * ((1) + cod4)
	print(round(servico, 2))