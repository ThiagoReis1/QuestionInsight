from numpy import *
v = array(eval(input("Digite distancia dos saltos: ")))

x = 0
y = 0
recorde = 2.5
while (y <= size(v)):
	if (v[x] <= recorde):
		x = x +1
	y = y - x
print(recorde)
print(y)


		 