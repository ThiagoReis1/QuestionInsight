from numpy import *
v = array(eval(input(":")))
i = 0
p = 0
while(v[i] <= 4):
	
	if(v[i]==1):
		p = p + 80
	elif(v[i] == 2):
		p = p + 40
	elif(v[i] == 3):
		p = p + 20 
	else:
		p = p + 10 
	i = i + 1
print(p)