from numpy import*
c = array(eval(input()))
a = 0
t = 0			 
while(a != size(c)):
	if(c[a]>80.0):
		t = t + (c[a] - c[a] * 0.15)
		a = a + 1
	else:
		t = t + c[a]
		a = a + 1
print(round(t,2))			  

