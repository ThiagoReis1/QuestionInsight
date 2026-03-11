x=float(input("digite um numero entre -1000 e 1000: "))
#y eh a funcao f(x)
if( x>=-1000 and x<-2):
	y = -(1/(x+2))
	print(round(y,4))
elif (x>2 and x<=1000):
	y = 1/(x-2)
	print(round(y,4))
else:
	print("'entrada invalida'")