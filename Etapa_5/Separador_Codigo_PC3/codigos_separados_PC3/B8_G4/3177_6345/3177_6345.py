from numpy import *

string = input("qtd de cada vogal: ")
v = ''
a = 0; e = 0; i = 0; o = 0; u = 0


for k in range(len(string)):
	if string == 'a':
		v = v + string[i]
		a += 1
		
	elif string == 'e':
		e += 1
		
	elif string == 'i':
		i += 1
		
	elif string == 'o':
		o += 1
		
	elif string == 'u':
		u += 1
	
print(a)
print(e)
print(i)
print(o)
print(u)