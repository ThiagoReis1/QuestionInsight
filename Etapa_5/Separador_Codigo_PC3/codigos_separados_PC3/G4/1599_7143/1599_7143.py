from numpy import*

c = array(eval(input("")))

i = 0
total = 0 

while(i < size(c)):
	if(i > 80):
		d = 0.15
		s = total + c-d
	else:
		s = total + c
	i = i + 1 
print(round(s, 2))
		
