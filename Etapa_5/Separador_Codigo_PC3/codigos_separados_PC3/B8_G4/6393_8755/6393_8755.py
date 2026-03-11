from numpy import * 
s = array(eval(input("digite aqui: ")))

for i in range(size(s)):
	if s[i] == 0:
		s[i] = 1**3
	elif s[i] == 1:
		s[i] = 2**3
	elif s[i] == 2:
		s[i] = 3**3
	elif s[i] == 3:
		s[i] = 4**3
	elif s[i] == 4:
		s[i] = 5**3
	elif s[i] == 5:
		s[i] = 6**3
	elif s[i] == 6:
		s[i] = 7**3
	elif s[i] == 7:
		s[i] = 8**3
	elif s[i] == 8:
		s[i] = 9**3
	elif s[i] == 9:
		s[i] = 0**3
print(s)