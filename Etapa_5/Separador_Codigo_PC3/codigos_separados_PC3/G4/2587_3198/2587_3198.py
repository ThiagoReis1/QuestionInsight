from numpy import*

v = array(eval(input("registro de velocidades: ")))
c = 0
for i in range(size(v)):
	p = (v[0] * 0.5) + v[0]
	if(v[i] > p):
		c = c + 1
		print(i)
print(c)
		