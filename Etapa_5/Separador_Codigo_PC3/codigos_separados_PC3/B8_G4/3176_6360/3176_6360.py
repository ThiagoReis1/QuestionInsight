from numpy import *
s = input()

vog = 0
con = 0
for i in range(len(s)):
	if s[i] in 'aeiou':
		vog = vog + 1
	elif s[i] in 'bcdfghjklmnpqrstvwxyz':
		con = con + 1
print(vog)
print(con)