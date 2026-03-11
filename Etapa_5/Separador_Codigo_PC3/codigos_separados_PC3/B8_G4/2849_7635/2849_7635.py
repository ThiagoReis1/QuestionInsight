from numpy import*

v = array(eval(input("")))
a = 0
for i in range(size(v)):
	if(v[i] != 0):
		v[i] = v[i]
		a = v[i] + a
		
	elif(v[i] == 0):
		a = a * 0
print(a)