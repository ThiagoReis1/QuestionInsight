from numpy import *

nts = array(eval(input(" ")))
ps = [3,2,4,1,3]

c = 0
nt = 0

while c < 5: 
	nt += nts[c] * ps[c] 
	c += 1
print(round(nt / sum(ps), 2)) 