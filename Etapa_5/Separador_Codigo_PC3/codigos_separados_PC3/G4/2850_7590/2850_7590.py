from numpy import*

v = array(eval(input("")))
j = 0

for i in range(size(v)):
	j = j + v[i]
	if(j>=55):
		j = 0
		
print(j)