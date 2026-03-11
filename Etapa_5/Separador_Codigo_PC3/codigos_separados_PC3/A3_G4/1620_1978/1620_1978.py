from numpy import*
t = array(eval(input()))
pa = array(eval(input()))
ct=0
l = 0
por=0
n = 1
k = len(t)
while(k > 0):
	l =  5 * (t[len(t) - n])
	por =  (pa[len(pa)- n])
	ct = (l * (por/100)) + ct
	k = k-1
	n = n + 1
print(round(ct,2))