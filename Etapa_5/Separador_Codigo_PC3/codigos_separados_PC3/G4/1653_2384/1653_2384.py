from numpy import*

s = input("string").split(',')
n = 0
a = 0
b = 1

for i in range (size(s)):
	if(s[a] == s[b]):
		n = n + 1
		b = b + 1
print(n)


