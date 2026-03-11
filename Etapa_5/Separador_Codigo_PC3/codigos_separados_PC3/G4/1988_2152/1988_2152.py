x = input("aminoacido: ").upper()

o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794

if(x == "ARGININA"):
	y = c*6+h*15+n*4+o*2
	print(round(y, 2))
elif(x == "TIROSINA"):
	y = c*9+h*11+n*1+o*3
	print(round(y, 2))
elif(x == "TRIPTOFANO"):
	y = c*11+h*11+n*2+o*2
	print(round(y, 2))
else:
	print("Entrada:", x)
	print("Dado Invalido")