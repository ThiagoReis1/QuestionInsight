r= input("digite o nome de um amonoacido: ")
o = 15.9994
c = 12.011
n = 14.0067
h = 1.00794
g = c*5+h*8+n*1+o*4
t = c*4+h*9+n*1+o*3

if(r.upper()=="GLUTAMINA"):
	print(round(g,2))
if(r.upper()=="TREONINA"):
	print(round(t,2))
