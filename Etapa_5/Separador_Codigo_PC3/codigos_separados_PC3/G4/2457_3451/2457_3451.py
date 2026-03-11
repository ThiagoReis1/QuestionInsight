q = int(input("q:"))
a = input("")


if(a=="rede"):
	p = 500.00 * q
	print(round(p, 2))
elif(a=="camarote"):
	p= 1200.00 * q
	print(round(p, 2))
elif(a=="suite"):
	p= 1500.00 * q
	print(round(p, 2))
else:
	print("acomodacao invalida")