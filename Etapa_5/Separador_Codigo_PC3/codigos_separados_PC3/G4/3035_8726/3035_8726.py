
from math import*
x = float(input("obra "))

if ( 0 <= x <90) or (180 <= x < 270):
	t = sin(radians(x)) 
	print(round(t,4))

elif(90 <=  x <180) or ( 270 <= x <360):
	t = cos(radians(x))
	print(round(t,4))
else:
	print("entrada invalida")