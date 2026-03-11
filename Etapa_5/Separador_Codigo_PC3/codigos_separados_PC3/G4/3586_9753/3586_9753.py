from numpy import * 
v = array(eval(input()))
i = 0
t = 0

while i < len(v):
	if v[i] == 1:
		t = t + 100
	if v[i] == 2:
		t = t + 60
	if v[i] == 3:
		t = t + 20
	if v[i] == 4:
		t = t + 0
	i += 1
print(t)