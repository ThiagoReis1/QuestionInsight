from numpy import *
n = array(eval(input()))
i = 0
t = 0
while i < size(n):
	if n[i] == 1:
		t += 10
	if n[i] == 2:
		t += 5
	if n[i] == 3:
		t += 10
	if n[i] == 4:
		t += 5
	if n[i] == 5:
		t += 10
	if n[i] == 6:
		t += 5
	i+=1
print(t)