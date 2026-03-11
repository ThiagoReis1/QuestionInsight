#
a=input('Cidade de destino:').lower()
b=int(input('Idade do passageiro:'))

p=500.00
sa=370.00
be=600.00
te=360.00
ta=550.00


#
if(a=='porto velho') and (b<=2) and (b>0):
	p=0.0
	print('Passagem: R$',p)

elif(a=='porto velho') and (b>=3) and (b<=12):
	p=500
	m=p/2
	print('Passagem: R$',m)
	
elif(a=='porto velho') and (b>=65):
	p=500.00
	m1=p*30/100
	m3=p-m1
	print('Passagem: R$',m3)
	
	
elif(a=='santarem') and (b<=2) and (b>0):
	sa=0.0
	print('Passagem: R$',sa)
	
elif(a=='santarem') and (b>=3)and (b<=12):
	sa=370.00
	m4=sa/2
	print('Passagem: R$',m4)

elif(a=='santarem') and (b>=65):
	sa=370.00
	m7=sa*30/100
	m8=sa-m7
	print('Passagem: R$',m8)
	
elif(a=='belem') and (b<=2) and (b>0):
	be=0.0
	print('Passagem: R$',be)
	
elif(a=='belem')and (b>=3) and (b<=12):
	be=600.00
	y1=be/2
	print('Passagem: R$',y1)
	
elif(a=='belem') and (b>=65):
	be=600.00
	y2=be*30/100
	y76=be-y2
	print('Passagem: R$',y76)
	
elif(a=='tefe')and (b<=2)and (b>0):
	te=0.0
	print('Passagem: R$',te)
	
elif(a=='tefe')and (b>=3)and (b<=12):
	te=360.00
	y34=te/2
	print('Passagem: R$',y34)
	
elif(a=='tefe')and (b>=65):
	te=360.00
	m87=te*30/100
	m88=te-m87
	print('Passagem: R$',m88)
	
	
elif(a=='tabatinga')and (b<=2)and (b>0):
	ta=0.0
	print('Passagem: R$',ta)
	
elif(a=='tabatinga')and (b>=3)and (b<=12):
	ta=550.00
	m876=ta/2
	print('Passagem: R$',m876)
elif(a=='tabatinga')and (b>65):
	ta=550.00
	m983=ta*30/100
	m54=ta-m983
	print('Passagem: R$',m54)
else:
	print('Entradas invalidas')