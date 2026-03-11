a= str(input("(T/P): ")).upper()
b= int(input("quantidade de t ou p: "))
c= int(input("quantidade de cappuccinos: "))

ttt= 6.00 * b + 4.50 * c

ttp= 5.00 * b + 4.50 * c

if a=="T":
	x= 6*b+4.50*c
	print(x)
else:
	y=5*b+4.50*c
	print(y)