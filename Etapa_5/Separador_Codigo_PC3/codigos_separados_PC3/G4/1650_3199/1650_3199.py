from numpy import *
s = input("cores de cabelo: ")
a = s.upper()
d = a.split(',')
p = 0 #num cabelos pretos
c = 0
r = 0
l = 0
b = 0
v = zeros(5, dtype=int)
for i in d:
	if i == 'P':
		p = p + 1
	if i == 'C':
		c = c + 1
	if i == 'R':
		r = r + 1
	if i == 'L':
		l = l + 1
	if i == 'B':
		b = b + 1

v[0] = p
v[1] = c
v[2] = r
v[3] = l
v[4] = b

print(max(v))
print(v)
