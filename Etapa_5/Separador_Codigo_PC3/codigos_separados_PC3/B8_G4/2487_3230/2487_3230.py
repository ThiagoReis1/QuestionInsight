a = int(input())
b = int(input())
c = int(input())

if((0<a<=4) and (0<b<=4) and (0<b<=4)):
	if(a==1):
		calc=180
	elif(a==2):
		calc=230
	elif(a==3):
		calc=250
	elif(a==4):
		calc=350
	if(b==1):
		cals=75
	elif(b==2):
		cals=110
	elif(b==3):
		cals=170
	elif(b==4):
		cals=200
	if(c==1):
		calb=20
	elif(c==2):
		calb=70
	elif(c==3):
		calb=100
	elif(c==4):
		calb=65
	t= calc+cals+calb	
	print("Entradas:", a,",", b,",", c)	
	print("Calorias:", t,"cal")
else :
	print("Entradas:", a,",", b,",", c)	
	print("Dados invalidos")