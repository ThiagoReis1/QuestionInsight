from numpy import *
temp = array(eval(input("insre essa merda")))
i = 0
x = 0
p = 0
while(i < 4):
	i = temp[x]
	x = x+1
	if(i == 1):
		p = p + 80
	elif(i == 2):
		p = p + 40
	elif(i == 3):
		p = p + 20
print(p)
		