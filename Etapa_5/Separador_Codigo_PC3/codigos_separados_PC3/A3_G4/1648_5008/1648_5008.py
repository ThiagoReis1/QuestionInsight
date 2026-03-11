from numpy import *
f = array(eval(input("f: ")))
r = 0
x = 0
n = 0
y = 0
for i in f:
	if i < 70:
		r += 1

v = zeros(r, dtype = int)
i = 0

for j in f:
	if j < 70:
		v[x] = i
		x += 1
	i += 1
print(r, v)