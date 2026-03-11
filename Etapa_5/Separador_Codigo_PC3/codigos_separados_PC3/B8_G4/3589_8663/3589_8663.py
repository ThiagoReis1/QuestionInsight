from numpy import*
n = array(eval(input( )))
i = 0
t = 0

while i < size(n):
	if n[i] == 1:
		t += 80
	elif n[i] == 2:
		t += 40
	elif n[i] == 3:
		t += 20
	elif n[i] == 4:
		t += 10
	i += 1
print(t)