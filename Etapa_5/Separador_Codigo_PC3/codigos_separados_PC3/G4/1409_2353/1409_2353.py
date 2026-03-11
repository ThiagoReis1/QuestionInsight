from math import*
a=str(input("Digite o tipo de ataque: "))
d1=int(input("Digite o valor do dado 1: "))
d2=int(input("Digite o valor do dado 2: "))
d3=int(input("Digite o valor do dado 3: "))
d4=int(input("Digite o valor do dado 4: "))

if(a=="espada"):
	print((d1+6)+(d2+6)+(d3+6)+(d4+6))
else:
	print((d1+d2+d3)*d4)