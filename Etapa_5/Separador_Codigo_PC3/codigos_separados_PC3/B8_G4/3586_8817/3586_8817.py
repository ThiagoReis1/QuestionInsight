from numpy import*

a = array(eval(input()))
t = 0
i = 0

while i < size(a) :
	if a[i] == 1:
		t = t + 100
	elif a[i] == 2:
		t = t + 60
	elif a[i] == 3:
		t = t + 20
	i = i + 1
print(t)