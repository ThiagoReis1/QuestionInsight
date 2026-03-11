from numpy import *
ent = input().upper()
n = len(ent)
v = zeros(4)
a = 0
b = 0
c = 0
d = 0
for i in ent:
	if (ent[i] == "A"):
		a += 1
		v[0] = a
print (v)

