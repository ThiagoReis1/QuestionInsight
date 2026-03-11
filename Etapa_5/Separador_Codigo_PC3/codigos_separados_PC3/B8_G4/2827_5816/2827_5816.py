from numpy import*
c = array(eval(input(": ")))
i = 0
while(i<len(c)):
	if(c[i] < 5 and c[i] > 4):
		c[i] =  4
	elif(c[i] < 10 and c[i] > 9):
		c[i] = 10
	i = i + 1	
print(c)