from numpy import*
v = input().split(',')
a = 0
b = 0
c = 0 
co= 0
u = 0
d = zeros(5, dtype= int)
for i in v:
	if(i == "AR"):
		a = a + 1
	elif(i == "BR"):
		b = b+1
	elif(i == "CL"):
		c = c + 1 
	elif(i == "CO"):
		co = co + 1
	elif(i == "UY"):
		u = u +1
d[0] = a
d[1] = b
d[2] = c
d[3] = co
d[4] = u
print(max(d))
print(d)