from numpy import*

v = eval(input("vai:"))

i = 0
c = 0

while(i < size(v)):
	if(v[i]>=50):
		t = v[i] - v[i]*0.08
	else:
		t = v[i]
	c = c + t
	i = i + 1
print(round(c,2))