from numpy import *
v = array(eval(input("demandas: ")))
x = v[0]
q = 0
for i in range(size(v)):
	if v[i] <= -x:
		q+=1
		print(i)
print(q)