from numpy import * 
x = array(eval(input("vetor")))
			 
c = 0
			 
while (x[c] < len(x)):
	x[c] = (x[c])**2
	c = c + 1
			 
y = (sum(x)/len(x))
print(y)
