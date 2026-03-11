##

a=float(input('Peso da encomenda em gramas:'))

##
b=(a*0.05)
c=(a*0.04+60)


##


if(a<5000):
	print(round(b,2))

else:
	print(round(c,2))