from numpy import*

nts = array(eval(input("")))
ps = array([3,2,4,1,3])

x = 0
i = 0

while (i < size(nts)):
	x = x + nts[i]*ps[i]
	i = i + 1
	y = sum(ps)
m = x/y
print(round(m, 2))