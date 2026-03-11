from math import *

x = float(input("Informe o valor de x: "))
i=0

if x <= 0:
	i=0
elif x > 0 and x <=1:
	i=1
	abs(i)
elif x > 1 and x <=2:
	i = x**(1/2)
	abs(i)
elif x > 2:
	i = x**(1/3)
	abs(i)

print(round(i, 4))