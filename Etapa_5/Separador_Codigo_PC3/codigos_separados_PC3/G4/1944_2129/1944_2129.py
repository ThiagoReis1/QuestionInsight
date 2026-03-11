a = input("nome do aminoacido: ")
a = a.lower()
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079
l = (c*6)+(h*13)+(n)+(o*2)
li = (c*6)+(h*15)+(n*2)+(o*2)
if a == "leucina":
   print(round(l,2))
else:
	print(round(li,2))
	