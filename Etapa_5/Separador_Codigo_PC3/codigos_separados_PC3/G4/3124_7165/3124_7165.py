from numpy import *
v = array(eval(input("vetor: ")))
M = 1
for x in range(size(v)):
	M = M *(v[x])
mg = (M)**(1/size(v))
print(round(mg, 2))

