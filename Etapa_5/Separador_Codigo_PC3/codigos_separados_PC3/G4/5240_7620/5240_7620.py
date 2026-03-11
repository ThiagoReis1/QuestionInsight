##
a=int(input('Consumo de energia:'))

##
if(a<100 and a>0):
	m=0.50*a+50
	print(round(m,2))
elif(a>=100 and a<250):
	m1=0.75*a+50
	print(round(m1,2))
	
elif(a>=250 and a<500):
	m2=1*a+50
	print(round(m2,2))
elif(a>=500):
	m3=1.25*a+50
	print(round(m3,2))
else:
	print('Valores invalidos')
	