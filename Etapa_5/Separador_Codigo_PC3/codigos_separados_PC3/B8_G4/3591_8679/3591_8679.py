from numpy import*

v = array(eval(input()))

i = 0
j = 0
p = 0

while i < size(v):
	if v[i] == 1 or v[i] == 3 or v[i] == 5:
		j = j + 10
	elif v[i] == 2 or v[i] == 4 or v[i] == 6:
		p = p + 5
	i = i + 1
s = j + p
print(s)