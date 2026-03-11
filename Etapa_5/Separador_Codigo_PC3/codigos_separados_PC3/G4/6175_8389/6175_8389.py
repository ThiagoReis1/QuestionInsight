from math import*

n = float(input(""))

if(n >= -4 and n < 0):
	fx = (abs(n))**(1/2)
	print(round(fx, 4))
	
elif(n >= 0 and n <= 4):
	fx = n**(1/2)
	print(round(fx, 4))
	
else:
	print("entrada invalida")