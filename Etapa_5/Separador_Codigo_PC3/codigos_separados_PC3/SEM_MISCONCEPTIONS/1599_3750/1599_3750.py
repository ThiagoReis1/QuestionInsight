from numpy import*
v = array(eval(input("")))
i = 0
c = 0
while(c <= size(v)):
	if(v[i] >= 80):
		f = v[i] *0.15
		v[i] -=f
		i = i + 1
	else :
		i = i + 1
	c = c + 1
   print(round(sum(v)))