from numpy import*

v1 = array(eval(input("BANANA" and "BIFE" and "FEIJOADA" and "OMELETE" and "TOMATE")))
v2 = array(eval(input()))


c = 0
s = 0

while(c < size(v1)):
	if(v1[c]=="BANANA"):
		s = s + (v2[c]*2)
		c = c + 1
	elif(v1[c]=="BIFE"):
		s = s + (v2[c]*2)
		c = c + 1
	elif(v1[c]=="FEIJOADA"):
		s = s + (v2[c]*2)
		c = c + 1
	elif(v1[c]=="OMELETE"):
		s = s + (v2[c]*2)
		c = c + 1
	elif(v1[c]=="TOMATE"):
		s = s + (v2[c]*2)
		c = c + 1
print(s)		