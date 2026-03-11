from numpy import * 
v = input("").upper()
conti = 0
contm = 0
conts = 0
i=0
t = 0
while i < len(v):
	if v[i] == 'I':
		conti = conti + 1 
		t = t + 3.75
	elif v[i] == 'M':
		contm = contm + 1
		t = t + 4.50
	elif v[i] == 'S':
		conts = conts + 1
		t = t + 2.90
	i = i +1
print(round(t,2), conti, contm, conts)



