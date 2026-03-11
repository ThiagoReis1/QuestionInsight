x=int(input(""))
y=int(input(""))
z=int(input(""))
if(1<=x<=4)and(1<=y<=4)and(1<=z<=4):
	if(x==1):
		w=180
	elif(x==2):
		w=230
	elif(x==3):
		w=250
	else:
		w=350
	
	if(y==1):
		p=75
	elif(y==2):
		p=110
	elif(y==3):
		p=170
	else:
		p=200
		
	if(z==1):
		k=20
	elif(z==2):
		k=70
	elif(z==3):
		k=100
	else:
		k=65
			
	print("Calorias:",(w+p+k),"cal")
else:
	print("Dados invalidos")