from numpy import*
c = array(eval(input()))
n = 1
k = len(c)
ct =0

while(k > 0):
	p =  (c[len(c)- n])
	ct = ct + (c[len(c)- n])
	k = k - 1
	n = n+1
	if(p > 80):
		ct = ct - 5
print(round(ct,2))