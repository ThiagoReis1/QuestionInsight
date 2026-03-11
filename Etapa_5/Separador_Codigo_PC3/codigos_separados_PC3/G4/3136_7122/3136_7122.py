from numpy import*

n = array(eval(input(": ")))

x = 0

for i in range(size(n)):
	x = x + log(n[i] + 1)
	
e = (exp(x/size(n)))-1
	

print(round(e,2))