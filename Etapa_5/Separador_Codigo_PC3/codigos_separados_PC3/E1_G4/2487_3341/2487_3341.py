a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if(a<0 or a>4 or c<0 or c>4 or b<0 or b>4):
	print("Entradas: ",a,",",b,",",c)
	print("Dados invalidos")
else:
	if(a==1):
		x = 180
	elif(a==2):
		x = 230
	elif(a==3):
		x = 250
	else:
		x = 350
		
	if(b==1):
		y = 75
	elif(b==2):
		y = 110
	elif(b==3):
		y = 170
	else:
		y = 200
			
	if(c==1):
		z = 20
	elif(c==2):
		z = 70
	elif(c==3):
		z = 100
	else:
		z = 65
	w = x + y + z	
	print("Entradas: ",a,",",b,",",c)
	print("Calorias: ",w,"cal")