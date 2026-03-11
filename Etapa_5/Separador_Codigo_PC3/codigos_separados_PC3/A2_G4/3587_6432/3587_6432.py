from numpy import *

pont = array(eval(input("")))

cont = 0
som = 100

while size(pont) > cont:
	if pont[cont] == 1:
		som = som * 5
	elif pont[cont] == 2: 
		som = som * 3
	elif pont[cont] == 4:
		som = som / 2
	else:
		som = som
	cont += 1
print(round(som,2))