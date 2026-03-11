aminoacido = input("")

o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
alanina = (c*3)+(h*7)+(n*1)+(o*2)
valina = (c*5)+(h*11)+(n*1)+(o*2)

if (aminoacido.upper() == "ALANINA"):
	print(float(round(alanina,2)))
else:
	print(float(round(valina, 2)))