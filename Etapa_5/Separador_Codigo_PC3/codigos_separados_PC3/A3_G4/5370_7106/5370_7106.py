from numpy import * 

v = array(eval(input()))
i = 0
val = "True"

while (i < size(v)-1):
	if v[i] >= v[i+1]:
		val = "False"
		
	i = i + 1
print(val)