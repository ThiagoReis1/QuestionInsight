a = input("Aminoacido:")
a = a.upper()
o = 15.9994
c = 12.011
n = 14.0067
h = 1.00794

if((a=="GLUTAMINA") or (a=="SERINA") or (a=="TREONINA")):
	if(a=="GLUTAMINA"):
		p = (5*c)+(8*h)+(n)+(4*o)
		print(round(p, 2))
	elif(a=="SERINA"):
		p = (3*c)+(7*h)+(n)+(3*o)
		print(round(p, 2))
	elif(a=="TREONINA"):
		p = (4*c)+(9*h)+(n)+(3*o)
		print(round(p, 2))
else:
	print("Entrada:", a)
	print("Dado Invalido")