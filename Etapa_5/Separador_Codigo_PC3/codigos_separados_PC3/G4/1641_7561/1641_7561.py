from numpy import *
v = array(eval(input("vetor: ")))
c =0
t =[]
for i in range (size(v)):
	if v[i] % 3 == 0:
		if (v[i]> 0):
			t.append(i)
			c = c+1
print (c)
print (t)