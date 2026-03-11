nome = input("Nome do aminoacido:(ARGININA ou TIROSINA) ")
amino = nome.upper()
c = 12.011
h = 1.00794
n = 14.00674
o = 15.9994

if(amino == "ARGININA"):
	a = c*6+h*15+n*4+o*2
	print(round(a,2))
else:
	t = c*9+h*11+n+o*3
	print(round(t,2))
	