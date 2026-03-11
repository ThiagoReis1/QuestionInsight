#Entrada
am = input("GLUTAMINA ou TREONINA? ")
#valores fixos
c = 12.011
h = 1.00794
n = 14.0067
o = 15.9994
#Formula
if(am.upper() == "GLUTAMINA"):
	d = ((c*5)+(h*8)+(n*1)+(o*4))
else:	
	d = ((4*c)+(9*h)+ n +(o*3))
	
print(round(d,2))