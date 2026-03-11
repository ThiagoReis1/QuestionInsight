from numpy import*
v = array(eval(input()))

a = 0
for i in v:
	if(i > 80):
		i = i 
		a = a + 1
print(round(sum(v),2))		