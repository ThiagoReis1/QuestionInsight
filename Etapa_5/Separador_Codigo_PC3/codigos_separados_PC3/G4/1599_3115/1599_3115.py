from numpy import*
n = array(eval(input("")))
c = 0
d = 15/100
while(c < size(n)):
	if(n[c]>80):
		n[c] = n[c] -n[c]*d
	else:
		n[c]=n[c]
	c = c + 1
print(round(sum(n),2))
	