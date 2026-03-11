from numpy import*
v = array(eval(input()))
i = 0
j = 0

while i < size(v):
	if v[i] < -60 or v[i] > 60:
		j += 1
	i += 1
v1 = array(zeros(size(v)-j, dtype = float))

i = 0
j = 0

while i < size(v):
	if -60.0 < v[i] < 60.0:
		v1[j] = v[i]
		j += 1
	i += 1
print(v1)