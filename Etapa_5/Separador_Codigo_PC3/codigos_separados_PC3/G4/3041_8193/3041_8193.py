x = float(input("x:"))

if (x>=-1000 and x<-2):
	a=-1/(x+2)
	print(round(a, 4))
elif (x>2 and x<=1000):
	b=1/(x-2)
	print(round(b, 4))
else:
	print("entrada invalida")