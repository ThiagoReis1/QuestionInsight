from numpy import *
v = array(eval(input("numero: ")))
i = 0
v2 = ""
exp = size(v)
while(i<size(v)):
	if(v[i] == v[-1]):
		v2 = v2 + str(v[i])
	else:
		v2 = v2 + str(v[i]) + "x^ "
	i = i + 1
print(v2)
	

 	
	