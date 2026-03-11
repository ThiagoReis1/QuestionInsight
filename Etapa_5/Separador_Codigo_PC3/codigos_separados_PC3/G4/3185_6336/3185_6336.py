from numpy import*

s = input("digite: ")
v = ''
i = -1 

while i >= -len(s):
	v = v + s[i]
	i = i - 1
	
print(v)