x=int(input("prato:"))
y=int(input("sobremesa:"))
z=int(input("bebida"))

print("Entradas:",x,",",y,",",z)

if(x<=4 and y<=4 and z<=4)and(x>0 and y>0 and z>0):
	
	if(x==1):p=180
	elif(x==2):p=230
	elif(x==3):p=250
	elif(x==4):p=350

	if(y==1):s=75
	elif(y==2):s=110
	elif(y==3):s=170
	elif(y==4):s=200
	
	if(z==1):b=20
	elif(z==2):b=70
	elif(z==3):b=100
	elif(z==4):b=65	
	
	vcal=p+s+b
	print("Calorias:",vcal,"cal")
	
else:
	print("Dados invalidos")


	

