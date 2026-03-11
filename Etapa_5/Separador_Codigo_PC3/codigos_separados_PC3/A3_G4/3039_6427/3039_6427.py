from math import*
x = float(input("leia o valor de x: "))
f = 0
if(x >= -1 and x < -1/2 or x > 1/2 and x <= 1):
	f = asin(x)
elif(x >= -1/2 and x <= 1/2):
	f = acos(x)
else:
	f = "entrada invalida"

print(round(f,2))
	
	
	
