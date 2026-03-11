x=int(input("Digite aqui um numero de 1 a 4:"))
y=int(input("Digite aqui um numero de 1 a 4:"))
z=int(input("Digite aqui um numero de 1 a 4:"))

print("Entradas: ", x, " , ", y, " , ",z)
if(x<=4 and y<=4 and z<=4 ):
	if(x<=4):
		if(x==1):
			x=180
		elif(x==2):
			x=230
		elif(x==3):
			x=250
		else:
			x=350
	if(y<=4):
		if(y==1):
			y=75
		elif(y==2):
			y=110
		elif(y==3):
			y=170
		else:
			y=200
	if(z<=4):
		if(z==1):
			z=20
		elif(z==2):
			z=70
		elif(z==3):
			z=100
		else:
			z=65
else:
	x=-1
	y=-1
	z=-1
soma=x+y+z	
if(soma!=-3):
	print("Calorias: ", soma, " cal")
else:
	print("Dados invalidos")

		
