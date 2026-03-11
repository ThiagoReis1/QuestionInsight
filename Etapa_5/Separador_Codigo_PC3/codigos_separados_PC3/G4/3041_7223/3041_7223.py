x = float(input("X: "))

if float(-1000<=x<-2):
	y=-(1/(x+2))
	print(round(y,4))
elif float(2<x<=1000):
	y=1/(x-2)
	print((round(y,4)))
else:
	print("entrada invalida")
	