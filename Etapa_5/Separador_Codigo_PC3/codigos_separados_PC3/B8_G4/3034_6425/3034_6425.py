from math import*
x=float(input("Entre com o valor de x: "))

if (x<-5 or x>5):
	print("entrada invalida")
else:
	if (x>=-4 and x<0):
		fx= abs(x)**(1/2) 
	elif (x==0):
		fx=0
	elif (x>0 and x <=4):
		fx= x**(1/2)
print(round(fx,4))
	
	
	
	