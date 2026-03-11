from numpy import *

anel = array(eval(input("Anel: ")))

i = 0
p1 = 80
p2 = 40
p3 = 20

s = 0


while (anel[i] > 0) and (anel[i] < 4):
	if(anel[i] == 1): 
		s = s + p1 
	elif(anel[i] == 2):
		s = s + p2 
	else:
		s = s + p3 
	i = i + 1


print(s)



