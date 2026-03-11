from numpy import *

v = array(eval(input()))
i = 0
s = "True"

while(i < size(v)-1):
	if(v[i+1] < v[i]):
		s = "False"
	i = i + 1
print(s)