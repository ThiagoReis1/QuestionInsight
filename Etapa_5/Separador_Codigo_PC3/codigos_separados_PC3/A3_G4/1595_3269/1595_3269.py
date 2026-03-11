from numpy import*
v = array(eval(input("")))
i = 0

for i in range(size(v)):
	x = sum(v)-min(v)
	s = x / size(v)
print(round(s, 2))
		
	
