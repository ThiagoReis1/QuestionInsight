aminoacido = input("nome do aminoacido: ")
aminoacido = aminoacido.upper()
o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
if (aminoacido == "ALANINA"): 
	print(round( c*3 + h*7 + n*1 + o*2, 2))
else:
	print(round( c*5 + h*11 + n*1 + o*2, 2))