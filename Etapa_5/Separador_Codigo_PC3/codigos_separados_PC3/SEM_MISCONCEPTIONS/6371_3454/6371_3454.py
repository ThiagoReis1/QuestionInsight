import numpy as np

password = eval(input())

cod = []
for p in password:
	c = p - 1
	if c == -1:
		c = 9
	
	cod.append(c**2)
		
print(np.array(cod))