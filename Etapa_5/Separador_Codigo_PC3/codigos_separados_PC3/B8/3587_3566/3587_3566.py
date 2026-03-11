from numpy import *

entrada = array(eval(input()))

total = 100
i = 0

while(i < size(entrada)):
	if(entrada[i] == 1):
		total = total * 5
	elif(entrada[i] == 2):
		total = total * 3
	elif(entrada[i] == 4):
		total = total / 2
	i+=1
	
print(round(total,2))
