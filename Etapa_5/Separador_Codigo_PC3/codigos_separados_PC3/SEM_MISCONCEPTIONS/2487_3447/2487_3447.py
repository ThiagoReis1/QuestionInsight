#numero do prato
x=float(input())
#numero da sobremesa
y=float(input())
#numero de bebida
z=float(input())

print("Entradas:",x,",",y,",",z)
if(x==1 or x==2 or x==3 or x==4):
	if((x==1):
		w=180
	elif(x==2):
		w=230
	elif(x==3):
  
elif(x==3):
	w=250
elif(x==4):
	w=350
#sobre
elif(y==1):
	v=75
elif(y==2):
	v=110
elif(y==3):
	v=170
elif(y==4):
	v=200
#bebida
elif(z==1):
	h=20
elif(z==2):
	h=70
elif(z==3):
	h=100
elif(z==4):
	h=65
	c = w + v + h 
	print("Calorias:",c,"cal")
else:
	print("Dados invalidos")