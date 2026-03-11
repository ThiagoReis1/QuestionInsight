c= input("Lanche ou salgado: ")
q= int(input("Quantidade de lanche ou salgado:  "))
r= int(input("Quantidade de refrigerante: "))

if(c.upper()=="L"):
	v= (5*q)+(r*4)
	print(round(v,2))
else:
	v=(3.5*q)+(r*4)
	print(round(v,2))