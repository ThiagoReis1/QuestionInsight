b = int(input("Digite a quantidade: "))
a = input("Digite a acomodacao: ")
r = 500
c = 1200
s = 1500
if (a=="rede"):
	print(b*r)
elif(a=="camarote"):
	print(b*c)
elif(a=="suite"):
	print(b*s)
else:
	print("acomodacao invalida")