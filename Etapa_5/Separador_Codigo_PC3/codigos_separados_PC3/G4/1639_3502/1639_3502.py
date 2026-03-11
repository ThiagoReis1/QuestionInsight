from numpy import*
v = array(eval(input('')))
t = 0
for x in v:
	if x %2 == 0:
		t += 1
print(t)
s = zeros(t, dtype=int)
j = 0
for k in range(size(v)):
	if v[k] %2 ==0:
		s[j] += k
		j += 1
print(s)
