x=float(input())
if(-100<=x<0):
	fx=-(1/x)
	print(round(fx,4))
elif(0<x<=100):
	fx=1/x
	print(round(fx,4))
else:
	print("entrada invalida")
