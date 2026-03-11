from numpy import
v = array(eval(input()))


for i in range(0, size(v)):
	if (0<=v or [i]<=8):
		v[i] = v[i] + 1
		elif (v[i]==9):
			v[i] = 0
print(v)