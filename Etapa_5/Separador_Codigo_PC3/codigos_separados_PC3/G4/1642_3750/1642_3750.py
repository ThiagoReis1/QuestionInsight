from numpy import * 
v = array(eval(input("")))
t = 0
for n in v :
	if(n % 5 == 0):
		t = t + 1
print(t)