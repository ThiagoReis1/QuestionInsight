from numpy import*
andares = array(eval(input("")))

i = 0
total = 0
while(i < size(andares)):
	total = total + (andares[i] - andares[i-1]) * 3
	i = i + 1 
print(total)	
