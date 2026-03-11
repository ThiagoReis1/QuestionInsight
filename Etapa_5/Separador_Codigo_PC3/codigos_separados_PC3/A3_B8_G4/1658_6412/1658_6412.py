from numpy import *
st= input('.').split(',')
j = 0
c = 0
t = 0
k = 0
m = 0
s = zeros(5 , dtype=int)
for i in range(size(st)):
	if st[i].upper() == 'JPN':
		s[1] = s[1] + 1
	elif st[i].upper() == 'CHN':
		s[0] = s[0] + 1
	elif st[i].upper() == 'KOR':
		s[2] = s[2] + 1
	elif st[i].upper() == 'MGL':
		s[3] = s[3] + 1
	elif st[i].upper() == 'THA':
		s[4] = s[4] + 1
print(max(s))
print(s)