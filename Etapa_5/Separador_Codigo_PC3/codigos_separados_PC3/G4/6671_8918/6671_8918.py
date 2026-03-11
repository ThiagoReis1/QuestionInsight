from numpy import *
v = array(eval(input("Digite aqui: ")))
c = 0
c1 = 0
for i in range(size(v)):
	if (v[i] > 15):
		c = c + v[i]
		c1 = c1 + 1
if (c1 == 0):
	print("0.0")
else: 
	me = c/c1
	print(round(me, 2))
		
		
		