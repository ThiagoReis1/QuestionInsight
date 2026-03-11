from numpy import*

v = array(eval(input("")))

i = 0
k = "True"

while i < size(v)-1:
	if v[i+1] < v[i]:
	
		k = "False"
	i = i + 1
print(k)