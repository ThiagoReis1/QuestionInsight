p=int(input("Qual o prato? "))
s=int(input("Qual o sobremesa? "))
b=int(input("Qual o bebida? "))

prato= (p==1 or p==2 or p==3 or p==4)
sobremesa= (s==1 or s==2 or s==3 or s==4)
bebida= (b==1 or b==2 or b==3 or b==4)

if not(prato and sobremesa and bebida):
	print("Entradas:",p,",",s,",",b)
	print("Dados invalidos")
else:
	#Pratos
	if p==1:
		p1=180
	elif p==2:
		p1=230
	elif p==3:
		p1=250
	elif p==4:
		p1=350
	#Sobremesas
	if s==1:
		s1=75
	elif s==2:
		s1=110
	elif s==3:
		s1=170
	elif s==4:
		s1=200
	#Bebidas
	if b==1:
		b1=20
	elif b==2:
		b1=70
	elif b==3:
		b1=100
	elif b==4:
		b1=65
	cal=p1+b1+s1
	print("Entradas:",p,",",s,",",b)
	print("Calorias:",cal,"cal")