from numpy import *
v = array(eval(input("numero: ")))
i = 0
j = -1
v2 = ""
exp = size(v) - 1
while(i<size(v)):
	if(v[i] == v[-1]):
		v2 = v2 + str(v[i])
	else:
		v2 = v2 + str(v[i]) + "x^ "+"+" +str(exp)
	i = i + 1
	j = j - 1
print(v2)

	

 	
	