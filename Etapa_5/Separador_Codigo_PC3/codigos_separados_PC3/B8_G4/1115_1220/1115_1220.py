x=float(input("Digite o salario: "))
y=int(input("Digite o codigo: "))
if(x>0):
	if(y==101):
		z=(x+(x*0.80/100))
	elif(y==102):
		z=(x+(x*0.65/100))
	elif(y==103):
		z=(x+(x*0.60/100))
	elif(y==104):
		z=(x+(x*0.55))
	print("Entradas: R$",x,"e","codigo",y)
	print("Novo salario: R$",round(z,2))
if(x<0):
	print("Entradas: R$",x,"e","codigo",y)
	print("Dado invalido")
	
	