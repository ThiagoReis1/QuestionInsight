from numpy import *

v = array(eval(input("v: ")))
i = 0
p = 0

if(v[i] == 1):
	p = p + 80
if(v[i] == 2):p = p + 40
elif(v[i] == 3):
p = p + 20
elif(v[i] == 4):
p = p + 10
else:
p = p + 10
		
print(p)
		