from numpy import *

v = array(eval(input("valor: ")))

vt = array([""])

c = 0  #conta
s = 0

while(c > len(v)):
	if(v[c] != " "):
		c = c + 1
	else:
		c = c + 1
		s = len(c) + 1
		
print(s)