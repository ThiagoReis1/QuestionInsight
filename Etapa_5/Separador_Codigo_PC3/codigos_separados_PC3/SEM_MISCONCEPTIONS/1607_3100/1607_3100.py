from numpy import*
a = array(eval(input()))
total = 0
c = 0
while(c < size(a)):
	if(c < size(a) and a[c]!= a[-1]):
		if(a[c + 1] - a[c] < 0):
			total = total + (-1*(a[c+1] - a[c])*3)
		else:
			total = total + ((a[c+1] - a[c])*3)	
		c = c + 1
	else:
		c = size(a)
print(total)
