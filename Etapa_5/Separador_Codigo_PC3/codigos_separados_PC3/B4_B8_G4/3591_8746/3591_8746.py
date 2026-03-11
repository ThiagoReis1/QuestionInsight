from numpy import*

v = array(eval(input("pts: ")))


c = 0

for x in v:
	if x == 1:
		
		c = c + 10
	elif x == 2:
		
		c = c + 5
	elif x == 3:
		
		c = c + 10
	elif x == 4:
		
		c = c + 5
	elif x == 5:
		
		c = c + 10
	elif x == 6:
		
		c = c + 5

print(c)