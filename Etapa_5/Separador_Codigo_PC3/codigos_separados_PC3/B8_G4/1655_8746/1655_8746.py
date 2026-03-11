from numpy import*

v = input("A: ").upper().split(',')

c = zeros(5, dtype=int)

for x in v:
	if x == "AC":
		c[0] = c[0] + 1
		
	elif x == "AM":
		c[1] = c[1] + 1
	elif x == "PA":
		c[2] = c[2] + 1
		
	elif x == "RO":
		c[3] = c[3] + 1
		
	elif x == "RR":
		c[4] = c[4] + 1
print(max(c))		
print(c)
