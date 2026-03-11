from numpy import*

a = input().upper()
r = 0
i = 0
t = 0
o = 0
e = 0
while i < len(a):
	if a[i] == "I":
		t = t + 3.75
		r = r + 1
	elif a[i] == "M":
		t = t + 4.50 
		o = o + 1
	elif a[i] == "S":
		t = t + 2.90
		e = e + 1
	i = i + 1
print(round(t,2), r,o,e)
#print(r + " " + o  + " " + e)