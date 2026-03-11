from numpy import *
v = array(eval(input("v: ")))
i = 0
p = 0
while(v[i] < 4):
	i = i + 1
	if(v[i] == 1):
		p = p + 80
	elif(v[i] == 2):
		p = p + 40
	else:
		p = p + 20
print(p)