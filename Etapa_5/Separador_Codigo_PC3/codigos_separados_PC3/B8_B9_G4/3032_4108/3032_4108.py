x = float (input("Digite o valor de x: "))
from math import *
if (x <= 0):
	f = 0
elif (x > 0 and x <= 1):
	f = 1
elif (x > 1 and x <= 2):
	f = abs((x)**0.5)
elif( x > 2):
	f = abs((x)**(1/3))
print (round(f,4))