from numpy import *
dif = array(eval(input("diferencas:")))
i = 0
s = 0
while(i < size(dif)):
	if(s <= 75):
		s = s + dif[i]
	elif(s > 75):
		s = 75
		s = s + dif[i]
	i = i + 1
print(s)	