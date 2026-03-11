nome=input("nome: (Aameul/Hethradiah)")
d1=int(input("d1:"))
d2=int(input("d2:"))
d3=int(input("d3:"))
if(nome=="Aameul"):
	dano=8+d1+d2+d3
	print(dano)
else:
	dano=2*(d1+d2+d3)
	print(dano)
	