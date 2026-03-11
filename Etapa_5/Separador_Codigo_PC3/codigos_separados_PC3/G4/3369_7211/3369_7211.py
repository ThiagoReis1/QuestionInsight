vel= (input("")).upper()
valor=float(input("valor da velocidade: "))
vkm=3.6*valor
vms=valor/3.6

if(vel == "K"):
	print(round(vms,2))
else:
	print(round(vkm,2))
	
	

