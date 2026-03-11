from numpy import *
n = input().upper()
i = 0
t = 0
u = 0
q = 0
v = 0
while i < len(n):
	if n[i] == "I":
		t += 3.75
		u+=1
	if n[i] == "M":
		t += 4.50
		q += 1
	if n[i] == "S":
		t += 2.90
		v += 1 
	i+=1
print(round(t,2), u, q, v)