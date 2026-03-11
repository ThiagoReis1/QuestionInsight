aminoacido = input("nome do aminoacido: ")
aminoacido = aminoacido.upper()
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
if (aminoacido  == "ASPARAGINA"):
	print(round( c*4 + h*8 + n*2 + o*3, 2))
else:
	print(round(c*11 + h*11 + n*2 + o*2, 2))