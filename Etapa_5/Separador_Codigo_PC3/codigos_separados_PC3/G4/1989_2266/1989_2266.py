at = input()
a = at.upper()

o = 15.999
c = 12.011
n = 14.00674
h = 1.00794

if a == "ASPARAGINA":
	peso = c*5+h*8+n*2+o*3
	print (round(peso,2))
elif a == "GLUTAMINA":
	peso = c*5+h*8+n*1+o*4
	print (round(peso,2))
elif a == "TRIPTOFANO":
	peso = c*11+h*11+n*2+o*2
	print (round(peso,2))
else:
	print ("Entrada:",a)
	print ("Dado Invalido")