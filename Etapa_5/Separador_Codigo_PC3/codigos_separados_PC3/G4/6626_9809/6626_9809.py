from numpy import *
n = input().upper()
t = len(n)
c = 0
cc = 0
while (c!=t):
	if (n[c]=='C'):
		cc+=1
	c +=1
print(cc)
