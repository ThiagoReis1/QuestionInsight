a=input("Digite o nome do aminoacido: ").lower()
o=15.999
c=12.011
n=14.00674
h=1.00794

if (a=="glutamina"):
	x=(5*c)+(8*h)+(1*n)+(4*o)
	print(round(x,2))
else:
	if (a=="histidina"):
		x=(6*c)+(10*h)+(3*n)+(2*o)
		print(round(x,2))
	else:
		if (a=="prolina"):
			x=(5*c)+(h*10)+(n*1)+(o*2)
			print(round(x,2))
		else:
			print("Entrada: ", a)
			print("Dado Invalido")