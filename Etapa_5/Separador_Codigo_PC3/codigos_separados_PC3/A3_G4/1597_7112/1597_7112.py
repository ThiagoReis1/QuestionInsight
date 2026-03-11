from numpy import*

v = array(eval(input("")))

i = 0 
t= sum(v)

while( i< size(v)):
	
	if v[i] > 80 :
		t = sum(v) - 5
	
	i = i +1
	


print(round(t,2))