from numpy import *

string = input('string:')

va = 0
ve = 0
vi = 0
vo = 0
vu = 0
for i in string:
	if i == 'a':
		va = va + 1
	elif i == 'e':
		ve = ve + 1
	elif i == 'i':
		vi = vi + 1
	elif i == 'o':
		vo = vo + 1
	elif i == 'u':
		vu = vu + 1
print('a:',va)
print('e:',ve)
print('i:',vi)
print('o:',vo)
print('u:',vu)
	

	

