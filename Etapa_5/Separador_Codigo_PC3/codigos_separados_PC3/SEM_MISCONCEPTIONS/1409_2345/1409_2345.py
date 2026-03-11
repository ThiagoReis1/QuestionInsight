ataque=input("espada ou cauda?")
d1=int(input("Valor do primeiro sorteio:"))
d2=int(input("Valor do segundo sorteio:"))
d3=int(input("Valor do terceiro sorteio:"))
d4=int(input("Valor do quarto sorteio:"))
ataque1= (d1+6)+(d2+6)+(d3+6)+(d4+6)
ataque2= (d1+d2+d3)*d4

if(ataque=="espada"):
	print(ataque1)
	
else:
	print(ataque2)