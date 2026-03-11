from numpy import*
v = array(eval(input("")))
d = 0
i = 0
s = 0
c= 0
while(i < size(v)):
	if(v[d] > 80):
		c = c + 5
		d = d + 1
	i =i + 1
	s = sum(v) - c
print(round(s,2))