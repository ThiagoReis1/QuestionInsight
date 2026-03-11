from numpy import *

v = array(eval(input("")))
j = input("")
total = 0
while(j < size(v)):
	if(j > 90):
		desconto = 6.50
		s = total + v - desconto
	else:
		s = total + v

print(round(s, 2))
