peso= int(input("peso: "))
d= int(input("distancia: "))
c= int(input("codigo: "))


if(c==1):
	icms=17/100
	servico=((peso * 25) + (d * 0.10)) + icms
	#preco= peso + d + icms
	#servico= preco * (icms/100)
	print(servico)
elif(c == 2):
	icms= 17.5
	servico= (peso * 25) + (d * 0.10) + (icms/100)
	#preco= peso + d + icms 
	print(servico)
elif(c==3):
	icms=18
	servico= (peso * 25) + (d * 0.10) + (icms/100)
	#preco= peso + d + icms 
	print(servico)
elif(c==4):
	icms=20
	servico= (peso * 25) + (d * 0.10) + (icms/100)
	#preco= peso + d + icms 
	print(servico)
	



