nome = input("digite o nome do aminoacido")
o = 15.9994
c = 12.011
n = 14.0067
h = 1.00794
if (nome.upper() == 'GLUTAMINA'):
	x = (c*5 + h*8 + n*1 + o*4)
	print(round(x,2))
	
if (nome.upper() == 'treonina'.upper()):
	y = (c*4 + h*9 + n + o*3)
	print(round(y,2))