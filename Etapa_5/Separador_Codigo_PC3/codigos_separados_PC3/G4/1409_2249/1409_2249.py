a=(input("Digite o tipo de golpe"))

d1=int(input("d1:"))
d2=int(input("d2:"))
d3=int(input("d3:"))
d4=int(input("d4:"))
if(a=="espada"):
	espadas= +6
	print(espadas)
else:
	caudas=(d1+d2+d3)*d4
	print(caudas)