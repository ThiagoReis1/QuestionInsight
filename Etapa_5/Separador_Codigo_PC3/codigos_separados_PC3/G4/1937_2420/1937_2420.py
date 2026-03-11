a = input("nome do aminoacido: ")
o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
if (a.upper()) == 'ALANINA':
   msg = (c*3) + (h*7) + (n) + (o*2)
else:
	msg = (c*5) + (h*11) + (n) + (o*2)
print(round(msg, 2))