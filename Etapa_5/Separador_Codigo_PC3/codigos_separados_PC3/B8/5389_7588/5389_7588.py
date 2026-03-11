from numpy import *

h = (str(input().upper()))

i =0

price = 0

while(i != len(h)):
	if(h[i] == 'A') or (h[i] == 'E') or (h[i] == 'I') or (h[i] == 'O') or (h[i] == 'U'):
		price += 3.15
	elif(h[i] != 'A') and (h[i] != 'E') and (h[i] != 'I') and (h[i] != 'O') and (h[i] != 'U'):
		price += 4.17
	i += 1

print(round(price, 2))