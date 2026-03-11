am = input(("glicina ou serina").upper())
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079
g = (c*2)+(h*5)+n+(o*2)
s = (c*3)+(h*7)+n+(o*3)
if ( am == "GLICINA"):
	print (round(g, 2))
else:
	print(round(s, 2))
