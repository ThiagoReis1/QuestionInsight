ataque = input("Diga o tipo de ataque:")
d1= int(input("Primeiro valor :"))
d2= int(input("Segundo valor :"))
d3= int(input("Terceiro valor :"))
d4= int(input("Quarto valor :"))
if(ataque=='espada'):
	n=(d1+d2+d3+d4)
	pontost=(n+(6*4))
	print(pontost)
else:
	pontost=((d1+d2+d3)*d4)
	print(pontost)