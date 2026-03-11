from numpy import *
v = array(eval(input("v: ")))

n = zeros(size(v), dtype=int)
e = 0

for i in range(size(v)):
	if v[i] == 0:
		n[i] = 9**2
	if v[i] == 1:
		n[i] = 0**2
	if v[i] == 2:
		n[i] = 1**2
	if v[i] == 3:
		n[i] = 2**2
	if v[i] == 4:
		n[i] = 3**2
	if v[i] == 5:
		n[i] = 4**2
	if v[i] ==6:
		n[i] = 5**2
	if v[i] == 7:
		n[i] = 6**2
	if v[i] == 8:
		n[i] = 7**2
	if v[i] == 9:
		n[i] = 8**2
print(n)