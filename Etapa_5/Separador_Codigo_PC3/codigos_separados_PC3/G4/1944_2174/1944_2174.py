amin =input("digite o aminoacido: ")

o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079

if(amin.lower()=="leucina"):
	x =(c*6) + (h*13) + n + (o*2)
	print(round(x, 2))
	
else:
	y = (c*6) + (h*15) + (n*2) + (o*2)
	print(round(y, 2))