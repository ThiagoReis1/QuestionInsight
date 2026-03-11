from numpy import*
s = input("string: ")
s = s.split(',')
i = 0
while(i < size(s)):
	s[i] = int(s[i])
	i += 1
print(sum(s))