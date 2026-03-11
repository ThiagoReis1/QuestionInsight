from numpy import * 

v = array(eval(input("v: ")))

i = 0 

while v[i] != min(v):
	i = i + 1
	
print(i)