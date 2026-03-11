from numpy import *

h = array(eval(input()))

h1 = zeros(size(h), dtype = float)

i = 0

while(i < size(h)):
	if(h[i] > 4) and (h[i] < 5):
		h[i] = 4.
	elif(h[i] > 9) and (h[i] < 10):
		h[i] = 10.
	i += 1

print(h)