from numpy import *

string = input().upper()

a = 0
e = 0
i = 0
o = 0
u = 0

for y in string:
	if y == 'A':
		a = a + 1
	elif y == 'E':
		e = e + 1
	elif y == 'I':
		i = i + 1
	elif y == 'O':
		o = o + 1
	elif y == 'U':
		u = u + 1
		
print("a: ", a)
print("e: ", e)
print("i: ", i)
print("o: ", o)
print("u: ", u)