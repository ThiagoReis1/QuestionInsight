x= int(input('prato: '))
y= int(input('sobremesa: '))
z= int(input('bebida: '))


if 0<x<5 and 0<y<5 and 0<z<5:
	if x==1:
		a=180
	
	elif x==2:
		a=230
	
	elif x==3:
		a=250
	
	elif x==4:
		a=350
		
	if y==1:
	   b=75
		
	elif y==2:
		b=110
		
	elif y==3:
		b=170
		
	elif y==4:
	   b=200
		
	if z==1:
		c=20
		
	elif z==2:
		c=70
		
	elif z==3:
		c=100
		
	elif z==4:
		c=65
		
	w=a+b+c
	
	print('Entradas:',x,',',y,',',z)	
	print('Calorias:',w,'cal')

else:
	print('Entradas:',x,',',y,',',z) 
	print('Dados invalidos')

