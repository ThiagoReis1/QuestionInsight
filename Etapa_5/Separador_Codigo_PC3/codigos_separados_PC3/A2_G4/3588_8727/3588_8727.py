from numpy import * 
x = array(eval(input("")))
s = 10000

i = 0
while i<size(x):
	if x[i]== 1:
		s = s*2
	if x[i] == 2:
		s = s 
	if x[i] == 3:
		s = s/2
	if x[i]== 4:
		s = s/4
	i = i +1
print(round(s,2))	
		